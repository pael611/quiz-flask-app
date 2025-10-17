from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from datetime import datetime
import random
import os
from dotenv import load_dotenv

load_dotenv()
from config import Config

# ==================== APP INITIALIZATION ====================

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_URL = "https://api.weatherapi.com/v1/forecast.json"
WEATHER_FORECAST_DAYS = 4
QUIZ_POINTS_PER_QUESTION = 10
LEADERBOARD_LIMIT = 10

# ==================== MODELS ====================

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    total_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    scores = db.relationship('UserScore', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'


class QuizQuestion(db.Model):
    __tablename__ = 'quiz_question'
    
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False, index=True)
    question = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    
    def __repr__(self):
        return f'<QuizQuestion {self.id}: {self.question[:50]}>'
    
    def get_options(self):
        """Return options as dictionary"""
        return {
            'A': self.option_a,
            'B': self.option_b,
            'C': self.option_c,
            'D': self.option_d
        }


class UserScore(db.Model):
    __tablename__ = 'user_score'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    score = db.Column(db.Integer, nullable=False)
    date_taken = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f'<UserScore user_id={self.user_id}, score={self.score}>'

# ==================== LOGIN MANAGER ====================

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))

# ==================== WEATHER SERVICE ====================

class WeatherService:
    """Service for weather API operations"""
    
    @staticmethod
    def get_forecast(city):
        """
        Fetch weather forecast for specified city
        
        Args:
            city (str): City name
            
        Returns:
            tuple: (weather_data, error_message)
        """
        if not API_KEY:
            error = "Weather API key not configured"
            return None, error
        
        try:
            params = {
                'key': API_KEY,
                'q': city,
                'days': WEATHER_FORECAST_DAYS,
                'aqi': 'no',
                'alerts': 'no'
            }
            
            response = requests.get(WEATHER_API_URL, params=params, timeout=5)
            response.raise_for_status()
            
            return WeatherService._parse_forecast(response.json()), None
        
        except requests.exceptions.RequestException as e:
            return None, f"Weather service error: {str(e)}"
        except (KeyError, ValueError) as e:
            return None, f"Invalid weather data: {str(e)}"
        except Exception as e:
            return None, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def _parse_forecast(data):
        """Parse weather API response into structured format"""
        if 'forecast' not in data:
            return None
        
        weather_list = []
        for day in data['forecast']['forecastday']:
            date_obj = datetime.strptime(day['date'], '%Y-%m-%d')
            
            weather_list.append({
                'date': day['date'],
                'day_name': date_obj.strftime('%A'),
                'day_temp': round(day['day']['maxtemp_c']),
                'night_temp': round(day['day']['mintemp_c']),
                'condition': day['day']['condition']['text'],
                'icon': day['day']['condition']['icon']
            })
        
        return weather_list if weather_list else None

# ==================== QUIZ SERVICE ====================

class QuizService:
    """Service for quiz operations"""
    
    @staticmethod
    def get_random_question():
        """Get random quiz question"""
        questions = QuizQuestion.query.all()
        if not questions:
            return None
        return random.choice(questions)
    
    @staticmethod
    def check_answer(question_id, answer):
        """
        Validate user answer
        
        Returns:
            tuple: (is_correct, correct_answer, question_object)
        """
        question = QuizQuestion.query.get(question_id)
        if not question:
            return None, None, None
        
        is_correct = answer.upper() == question.correct_answer
        return is_correct, question.correct_answer, question
    
    @staticmethod
    def update_user_score(user, points):
        """Update user score after correct answer"""
        user.total_score += points
        db.session.commit()
        
        score_record = UserScore(user_id=user.id, score=points)
        db.session.add(score_record)
        db.session.commit()
    
    @staticmethod
    def get_leaderboard(limit=LEADERBOARD_LIMIT):
        """Get top players leaderboard"""
        return db.session.query(User).order_by(User.total_score.desc()).limit(limit).all()

# ==================== AUTH SERVICE ====================

class AuthService:
    """Service for authentication operations"""
    
    @staticmethod
    def validate_registration(username, nickname, password, confirm_password):
        """
        Validate registration data
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not all([username, nickname, password]):
            return False, 'Semua field harus diisi!'
        
        if password != confirm_password:
            return False, 'Password tidak cocok!'
        
        if User.query.filter_by(username=username).first():
            return False, 'Username sudah digunakan!'
        
        if User.query.filter_by(nickname=nickname).first():
            return False, 'Nickname sudah digunakan!'
        
        return True, None
    
    @staticmethod
    def create_user(username, nickname, password):
        """Create new user"""
        user = User(
            username=username,
            nickname=nickname,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def authenticate_user(username, password):
        """Authenticate user by username and password"""
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            return user
        return None

# ==================== ROUTES - AUTH ====================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        nickname = request.form.get('nickname', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        is_valid, error = AuthService.validate_registration(
            username, nickname, password, confirm_password
        )
        
        if not is_valid:
            return render_template('register.html', error=error)
        
        AuthService.create_user(username, nickname, password)
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        user = AuthService.authenticate_user(username, password)
        
        if user:
            login_user(user)
            return redirect(url_for('index'))
        
        return render_template('login.html', error='Username atau password salah!')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """User logout route"""
    logout_user()
    return redirect(url_for('index'))

# ==================== ROUTES - MAIN ====================

@app.route('/')
def index():
    """Home page with weather widget"""
    city = request.args.get('city', 'Jakarta').strip()
    weather_data, error = WeatherService.get_forecast(city) if city else (None, None)
    
    return render_template(
        'index.html',
        weather_data=weather_data,
        city=city,
        error=error
    )

# ==================== ROUTES - QUIZ ====================

@app.route('/quiz')
@login_required
def quiz():
    """Quiz page"""
    return render_template('quiz.html', user_score=current_user.total_score)


@app.route('/api/quiz/next-question', methods=['GET'])
@login_required
def next_question():
    """API: Get next quiz question"""
    question = QuizService.get_random_question()
    
    if not question:
        return jsonify({'error': 'Tidak ada pertanyaan tersedia'}), 404
    
    return jsonify({
        'id': question.id,
        'question': question.question,
        'options': question.get_options()
    })


@app.route('/api/quiz/submit-answer', methods=['POST'])
@login_required
def submit_answer():
    """API: Submit quiz answer"""
    data = request.get_json() or {}
    question_id = data.get('question_id')
    answer = data.get('answer', '')
    
    is_correct, correct_answer, question = QuizService.check_answer(question_id, answer)
    
    if is_correct is None:
        return jsonify({'error': 'Pertanyaan tidak ditemukan'}), 404
    
    if is_correct:
        QuizService.update_user_score(current_user, QUIZ_POINTS_PER_QUESTION)
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': correct_answer,
        'new_score': current_user.total_score
    })

# ==================== ROUTES - LEADERBOARD ====================

@app.route('/leaderboard')
def leaderboard():
    """Leaderboard page"""
    top_players = QuizService.get_leaderboard()
    return render_template('leaderboard.html', players=top_players)

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('error.html', error='Halaman tidak ditemukan'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('error.html', error='Terjadi kesalahan server'), 500

# ==================== DATABASE INITIALIZATION ====================

def init_sample_questions():
    """Initialize sample quiz questions"""
    if QuizQuestion.query.count() > 0:
        return
    
    questions = [
        QuizQuestion(
            topic='AI Development',
            question='Python library mana yang paling populer untuk machine learning?',
            option_a='NumPy',
            option_b='Scikit-learn',
            option_c='Pandas',
            option_d='Matplotlib',
            correct_answer='B'
        ),
        QuizQuestion(
            topic='AI Development',
            question='Apa kepanjangan dari NLP?',
            option_a='Neural Learning Process',
            option_b='Natural Language Processing',
            option_c='Neurological Language Pattern',
            option_d='Network Learning Protocol',
            correct_answer='B'
        ),
        QuizQuestion(
            topic='Computer Vision',
            question='Library mana yang sering digunakan untuk Computer Vision?',
            option_a='TensorFlow',
            option_b='OpenCV',
            option_c='Keras',
            option_d='PyTorch',
            correct_answer='B'
        ),
        QuizQuestion(
            topic='AI Development',
            question='Apa yang dimaksud dengan Deep Learning?',
            option_a='Pembelajaran menggunakan neural network dengan banyak layer',
            option_b='Pembelajaran dengan data yang sangat besar',
            option_c='Pembelajaran menggunakan komputer berkekuatan tinggi',
            option_d='Pembelajaran untuk masalah yang sangat kompleks',
            correct_answer='A'
        ),
        QuizQuestion(
            topic='Computer Vision',
            question='CNN digunakan untuk?',
            option_a='Text classification',
            option_b='Image recognition',
            option_c='Time series prediction',
            option_d='Natural language generation',
            correct_answer='B'
        ),
    ]
    
    db.session.add_all(questions)
    db.session.commit()


def init_db():
    """Initialize database"""
    with app.app_context():
        db.create_all()
        init_sample_questions()

# ==================== MAIN ====================

if __name__ == '__main__':
    init_db()
    app.run(debug=True)