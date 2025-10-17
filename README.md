# Quiz Academy 🧠

Situs web kuis dinamis interaktif yang ditujukan untuk audiens remaja, dengan fitur autentikasi, papan peringkat real-time, dan widget prakiraan cuaca. Dibangun menggunakan Flask dengan SQLite database lokal.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Struktur Project](#struktur-project)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Troubleshooting](#troubleshooting)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## ✨ Fitur Utama

### 🔐 Autentikasi

- Registrasi pengguna dengan validasi username dan nickname unik
- Login dengan enkripsi password menggunakan Werkzeug
- Logout dengan session management Flask-Login
- Password hashing aman

### 🎯 Sistem Kuis

- Pertanyaan kuis dengan 4 pilihan jawaban (A, B, C, D)
- Pertanyaan ditampilkan secara acak tanpa batas
- Sistem poin: 10 poin per jawaban benar
- Total skor tersimpan di akun pengguna
- Riwayat skor pengguna

### 📊 Papan Peringkat

- Menampilkan top 10 pemain berdasarkan total skor
- Ranking otomatis berdasarkan performa
- Informasi tanggal registrasi pemain
- Highlight pemain yang sedang login
- Update real-time setelah setiap kuis

### 🌤️ Widget Prakiraan Cuaca

- Pencarian cuaca berdasarkan nama kota
- Prakiraan 4 hari ke depan (real-time dari WeatherAPI)
- Menampilkan suhu siang dan malam
- Ikon dan kondisi cuaca dengan detail
- Nama hari dalam bahasa Inggris

### 📱 User Interface

- Navigasi menu responsif dengan brand logo
- Desain mobile-friendly dan modern
- Footer dengan informasi pengembang
- Error handling yang user-friendly
- Loading states dan feedback visual
- Gradient backgrounds dan smooth transitions

### 📚 Topik Kuis

- Pengembangan AI dengan Python
- Computer Vision
- Natural Language Processing (NLP)
- Implementasi Model AI
- 5+ pertanyaan sample siap pakai

## 🛠️ Teknologi yang Digunakan

### Backend

- **Flask** (2.3.2) - Web framework Python
- **Flask-SQLAlchemy** (3.0.5) - ORM untuk database
- **Flask-Login** (0.6.2) - User session management
- **Werkzeug** (2.3.6) - Security utilities & password hashing
- **SQLAlchemy** (2.0.19) - Database ORM layer

### Database

- **SQLite** - Lightweight local database (file-based)
- **quiz_academy.db** - Auto-created pada first run

### Frontend

- **Jinja2** - Template engine (built-in Flask)
- **HTML5** - Semantic markup
- **CSS3** - Modern styling & responsive design
- **JavaScript (Vanilla)** - Client-side interactivity

### External APIs

- **WeatherAPI** (weatherapi.com) - Prakiraan cuaca real-time

### Development Tools

- **Python 3.8+** - Programming language
- **pip** - Package manager
- **python-dotenv** - Environment variables management
- **Virtual Environment** - Project isolation

## 📦 Library & Dependencies

Lihat file `DEPENDENCIES.md` untuk penjelasan lengkap setiap library.

**Ringkas:**
```
pip install -r requirements.txt
```

Installs:
- Flask, Werkzeug, Flask-SQLAlchemy, SQLAlchemy
- Flask-Login, requests, python-dotenv

## 📋 Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- **Python** 3.8 atau lebih tinggi
- **pip** (Python package manager) - usually comes with Python
- **git** (untuk version control) - optional
- **API key WeatherAPI** (gratis di [weatherapi.com](https://www.weatherapi.com))
- **Text Editor/IDE** - VS Code, PyCharm, atau Sublime Text
- **Internet connection** - untuk WeatherAPI

### Verifikasi Prerequisites

```bash
python --version          # Harus 3.8+
pip --version            # Harus ada
git --version            # Optional, untuk git
```

## 🚀 Instalasi

### Step 1: Clone atau Download Project

```bash
# Via Git
git clone https://github.com/username/kodlab-quiz-academy.git
cd kodlab-quiz-academy

# Atau download ZIP dan extract
cd c:\Users\pael\Documents\pengumpulan dicoding\kodlab
```

### Step 2: Buat Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed Flask-2.3.2 Flask-Login-0.6.2 ...
```

### Step 4: Setup Environment Variables

Buat file `.env` di root folder project:

```properties
WEATHER_API_KEY=f8e66e4cb2434da297b73204251710
SECRET_KEY=lms-app-flask
FLASK_ENV=development
```

### Step 5: Verify Installation

```bash
# Test database connection
python test_connection.py

# Debug database
python debug_db.py
```

Expected output:
```
✅ ALL TESTS PASSED - LOCAL DATABASE READY!
```

### Step 6: Jalankan Aplikasi

```bash
python app.py
```

Expected output:
```
WARNING: This is a development server. Do not use it in production.
Running on http://127.0.0.1:5000
```

Akses aplikasi di: **http://localhost:5000**

## ⚙️ Konfigurasi

### Environment Variables (.env)

File `.env` berisi:
```properties
# Weather API Key
WEATHER_API_KEY=your-api-key-here

# Flask Secret Key (untuk session)
SECRET_KEY=your-secret-key-change-in-production

# Flask Environment
FLASK_ENV=development  # atau production
```

### Database Configuration

Database otomatis dibuat saat app first run:
- **File:** `quiz_academy.db` (di root folder)
- **Type:** SQLite (file-based)
- **Tables:** user, quiz_question, user_score

Untuk manual creation:
```bash
python create_db.py
```

### Config File (config.py)

```python
# Database URI (otomatis SQLite)
SQLALCHEMY_DATABASE_URI = "sqlite:///quiz_academy.db"

# Security
SECRET_KEY = "lms-app-flask"

# API
WEATHER_API_KEY = "dari .env"
```

## 🎮 Menjalankan Aplikasi

### Development Mode

```bash
python app.py
```

Akses: `http://localhost:5000`

**Apa yang terjadi saat pertama kali run:**
1. ✅ File `quiz_academy.db` dibuat otomatis di root folder
2. ✅ Tabel-tabel database dibuat otomatis
3. ✅ 5 sample quiz questions diisi ke database
4. ✅ Database siap untuk digunakan

### Operasi Database

```bash
# Membuat database manual
python create_db.py

# Test koneksi database
python test_connection.py

# Debug database
python debug_db.py

# Create database dalam Python interactive shell
python
>>> from app import app, db, init_db
>>> init_db()
```

## 📁 Struktur Project

```
kodlab/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (git ignored)
├── .gitignore                     # Git ignore file
├── README.md                      # Project documentation
├── DEPENDENCIES.md                # Library documentation
├── INSTALLATION.md                # Detailed installation guide
│
├── quiz_academy.db                # SQLite database (auto-created)
├── create_db.py                   # Manual database creation script
├── test_connection.py             # Database connection test
├── debug_db.py                    # Database debugging script
├── check_network.py               # Network diagnostic script
│
├── templates/                     # HTML templates
│   ├── base.html                 # Base template dengan navbar & footer
│   ├── index.html                # Home page dengan weather widget
│   ├── register.html             # Registration form
│   ├── login.html                # Login form
│   ├── quiz.html                 # Quiz interface
│   ├── leaderboard.html          # Papan peringkat
│   └── error.html                # Error page
│
├── static/                        # Static files
│   ├── css/
│   │   └── style.css             # Main stylesheet (responsive)
│   └── js/
│       └── script.js             # Client-side logic
│
└── docs/                          # Documentation
    ├── PYTHONANYWHERE_SETUP.md   # PythonAnywhere deployment
    ├── SUPABASE_FIREWALL_SETUP.md # Network setup (archived)
    └── WSGI.md                   # WSGI configuration
```

## 🗄️ Database

### Schema

**users table:**
```
id (Primary Key)
username (String, Unique)
nickname (String, Unique)
password (String, hashed)
total_score (Integer)
created_at (DateTime)
```

**quiz_question table:**
```
id (Primary Key)
topic (String)
question (String)
option_a, option_b, option_c, option_d (String)
correct_answer (String: A/B/C/D)
```

**user_score table:**
```
id (Primary Key)
user_id (Foreign Key → user.id)
score (Integer)
date_taken (DateTime)
```

### Database Features

✅ **Auto-creation:**
- Database file otomatis dibuat saat app startup
- Tabel otomatis dibuat dengan `db.create_all()`
- Sample questions otomatis diisi

✅ **Persistence:**
- Data tersimpan di file `quiz_academy.db`
- Data persisten antar session
- Backup: copy file `quiz_academy.db`
- Reset: delete file, database akan recreate

✅ **Performance:**
- SQLite optimal untuk single-user/development
- Connection timeout: 10 detik
- Pool pre-ping untuk connection health check

## 🔌 API Endpoints

### Authentication Routes
```
POST   /register       # Register pengguna baru
POST   /login          # Login pengguna
GET    /logout         # Logout (require login)
```

### Main Routes
```
GET    /               # Home page dengan weather widget
GET    /quiz           # Quiz page (require login)
GET    /leaderboard    # Papan peringkat
```

### Quiz API
```
GET    /api/quiz/next-question           # Get random question (JSON)
POST   /api/quiz/submit-answer           # Submit answer (JSON)
```

**Quiz API - Request/Response:**

Get Question:
```bash
GET /api/quiz/next-question
```

Response:
```json
{
  "id": 1,
  "question": "Python library mana yang paling populer untuk machine learning?",
  "options": {
    "A": "NumPy",
    "B": "Scikit-learn",
    "C": "Pandas",
    "D": "Matplotlib"
  }
}
```

Submit Answer:
```bash
POST /api/quiz/submit-answer
Content-Type: application/json

{
  "question_id": 1,
  "answer": "B"
}
```

Response:
```json
{
  "correct": true,
  "correct_answer": "B",
  "new_score": 50
}
```

## 🎓 Topik Kuis & Pertanyaan

### AI Development
- Machine Learning libraries
- Natural Language Processing
- Deep Learning concepts
- Python untuk AI

### Computer Vision
- OpenCV library
- CNN (Convolutional Neural Networks)
- Image recognition
- Visual processing

### Pertanyaan Sample
5 sample questions sudah included:
1. ML library terpopuler
2. Pengertian NLP
3. Computer Vision library
4. Deep Learning definition
5. CNN usage

Tambah pertanyaan di `init_sample_questions()` di app.py

## 🔒 Security Features

- ✅ Password hashing dengan Werkzeug (PBKDF2)
- ✅ SQL injection prevention via SQLAlchemy ORM
- ✅ CSRF protection built-in Flask-Login
- ✅ Environment variables untuk sensitive data
- ✅ Username & nickname uniqueness validation
- ✅ Input sanitization di forms
- ✅ Session management secure

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (PythonAnywhere)
1. Upload project files
2. Create virtual environment
3. Install dependencies
4. Configure WSGI file
5. Set environment variables
6. Configure static files
7. Reload web app

Lihat `PYTHONANYWHERE_SETUP.md` untuk detail lengkap.

### Production (Self-hosted)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🐛 Troubleshooting

### Database Issues

**Problem:** "database is locked"
```bash
# Solusi: Restart aplikasi
python app.py
```

**Problem:** "no such table"
```bash
# Solusi: Recreate database
rm quiz_academy.db
python create_db.py
```

### Import Errors

**Problem:** "ModuleNotFoundError: No module named 'flask'"
```bash
# Solusi: Install dependencies
pip install -r requirements.txt
```

### Weather API Issues

**Problem:** "Weather API key not configured"
```bash
# Solusi: Set WEATHER_API_KEY di .env
WEATHER_API_KEY=your-key-here
```

**Problem:** "Invalid weather data"
```bash
# Solusi: Verify city name
# Try: Jakarta, London, New York, etc.
```

### Logging & Debug

```bash
# Test database
python test_connection.py

# Debug database
python debug_db.py

# Check app logs
tail -f app.log
```

## 📊 Performance & Optimization

- SQLite optimal untuk development
- Connection pooling built-in
- Query optimization dengan indexes
- Static file caching
- Lazy loading untuk relationships

Untuk production dengan many users, consider migrate ke PostgreSQL/MySQL

## 📝 Best Practices Implemented

✅ Service Layer Architecture (WeatherService, QuizService, AuthService)
✅ Separation of Concerns (Models, Routes, Services)
✅ Error Handling & Logging
✅ Input Validation & Sanitization
✅ Security (Password hashing, SQL injection prevention)
✅ Responsive Design
✅ RESTful API patterns
✅ Code Comments & Documentation

## 👨‍💻 Author

**Developer:** Pael Siregar  
**Project:** Quiz Academy - Educational Quiz Platform  
**Created:** 2024  
**For:** Dicoding Course - Python Web Development  

## 📜 Lisensi

Project ini open source dan dapat digunakan untuk tujuan pembelajaran dan komersial.

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk kontribusi:

1. Fork repository
2. Buat branch feature (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## 💬 Support

Jika ada pertanyaan atau issues:
- Buka issue di GitHub
- Cek dokumentasi: README.md, DEPENDENCIES.md, INSTALLATION.md
- Jalankan diagnostic scripts: test_connection.py, debug_db.py

## 📚 Dokumentasi Tambahan

- `DEPENDENCIES.md` - Penjelasan setiap library
- `INSTALLATION.md` - Panduan instalasi lengkap
- `PYTHONANYWHERE_SETUP.md` - Deploy ke PythonAnywhere

## 🎉 Terima Kasih

Terima kasih telah menggunakan Quiz Academy! Semoga project ini bermanfaat untuk pembelajaran web development dengan Flask.

---

**Last Updated:** Desember 2024  
**Version:** 1.0.0 (SQLite Local)  
**Database:** SQLite (quiz_academy.db)  
**Status:** ✅ Production Ready
