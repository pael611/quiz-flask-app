# Quiz Academy 🧠

Situs web kuis dinamis interaktif yang ditujukan untuk audiens remaja, dengan fitur autentikasi, papan peringkat real-time, dan widget prakiraan cuaca. Dibangun menggunakan Flask dan PostgreSQL.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Struktur Project](#struktur-project)
- [API Endpoints](#api-endpoints)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## ✨ Fitur Utama

### 🔐 Autentikasi

- Registrasi pengguna dengan validasi username dan nickname unik
- Login dengan enkripsi password
- Logout dengan session management

### 🎯 Sistem Kuis

- Pertanyaan kuis dengan 4 pilihan jawaban (A, B, C, D)
- Pertanyaan ditampilkan secara acak tanpa batas
- Sistem poin: 10 poin per jawaban benar
- Total skor tersimpan di akun pengguna

### 📊 Papan Peringkat

- Menampilkan top 10 pemain
- Ranking berdasarkan total skor
- Informasi tanggal registrasi pemain
- Highlight pemain yang login

### 🌤️ Widget Prakiraan Cuaca

- Pencarian cuaca berdasarkan nama kota
- Prakiraan 3 hari ke depan
- Menampilkan suhu siang dan malam
- Ikon dan kondisi cuaca real-time

### 📱 User Interface

- Navigasi menu responsif
- Desain mobile-friendly
- Footer dengan informasi pengembang
- Error handling yang user-friendly

### 📚 Topik Kuis

- Pengembangan AI dengan Python
- Computer Vision
- Natural Language Processing (NLP)
- Implementasi Model AI

## 🛠️ Teknologi yang Digunakan

### Backend

- **Flask** (2.3.2) - Web framework
- **Flask-SQLAlchemy** (3.0.5) - ORM untuk database
- **Flask-Login** (0.6.2) - User session management
- **Werkzeug** (2.3.6) - Security utilities

### Database

- **PostgreSQL** - Database relasional
- **Supabase** - PostgreSQL managed service

### Frontend

- **Jinja2** - Template engine
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript** - Client-side logic

### External APIs

- **WeatherAPI** - Prakiraan cuaca real-time

### Development Tools

- **Python 3.8+**
- **pip** - Package manager
- **python-dotenv** - Environment variables

## 📦 Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Account Supabase (gratis di [supabase.com](https://supabase.com))
- API key WeatherAPI (gratis di [weatherapi.com](https://www.weatherapi.com))
- Git (untuk version control)

## 🚀 Instalasi

### 1. Clone Repository

\`\`\`bash
git clone https://github.com/username/kodlab-quiz-academy.git
cd kodlab-quiz-academy
\`\`\`

### 2. Buat Virtual Environment

**Windows:**
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

**macOS/Linux:**
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## ⚙️ Konfigurasi

### 1. Setup Environment Variables

Buat file `.env` di root folder:

\`\`\`properties

# Supabase PostgreSQL Configuration

SUPABASE_USER=postgres.jazasgfuqqnlezgarykz
SUPABASE_PASSWORD=your-actual-password
SUPABASE_HOST=aws-1-us-east-1.pooler.supabase.com
SUPABASE_PORT=6543
SUPABASE_DBNAME=postgres

# Security

SECRET_KEY=your-secret-key-here

# Weather API

WEATHER_API_KEY=your-weatherapi-key-here

# Flask

FLASK_ENV=development
\`\`\`

### 2. Dapatkan Credentials

#### Supabase Database

1. Daftar di [supabase.com](https://supabase.com)
2. Buat project baru
3. Pergi ke Settings → Database → Connection Pooler
4. Pilih "PgBouncer" dan salin credentials

#### WeatherAPI Key

1. Daftar di [weatherapi.com](https://www.weatherapi.com)
2. Dapatkan API key gratis di dashboard
3. Tambahkan ke file `.env`

### 3. Test Koneksi Database

\`\`\`bash
python test_connection.py
\`\`\`

Output yang diharapkan:
\`\`\`
✅ ALL TESTS PASSED - CONNECTION IS WORKING!
\`\`\`

## 🎮 Menjalankan Aplikasi

### Development Mode

\`\`\`bash
python app.py
\`\`\`

Akses aplikasi di: `http://localhost:5000`

### Production Mode (PythonAnywhere)

1. Upload project ke PythonAnywhere
2. Setup virtual environment
3. Configure WSGI file
4. Set SECRET_KEY yang aman
5. Update FLASK_ENV ke 'production'

## 📁 Struktur Project

\`\`\`
kodlab/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (git ignored)
├── README.md                      # Project documentation
├── test_connection.py             # Database connection test
├── templates/
│   ├── base.html                 # Base template dengan navbar & footer
│   ├── index.html                # Home page dengan weather widget
│   ├── register.html             # Registration page
│   ├── login.html                # Login page
│   ├── quiz.html                 # Quiz page
│   ├── leaderboard.html          # Leaderboard page
│   └── error.html                # Error page
├── static/
│   ├── css/
│   │   └── style.css             # Main stylesheet
│   └── js/
│       └── script.js             # Client-side logic
└── .gitignore                    # Git ignore file
\`\`\`

## 🔌 API Endpoints

### Authentication

- `POST /register` - Registrasi pengguna baru
- `POST /login` - Login pengguna
- `GET /logout` - Logout pengguna (require login)

### Pages

- `GET /` - Home page dengan weather widget
- `GET /quiz` - Quiz page (require login)
- `GET /leaderboard` - Papan peringkat

### Quiz API

- `GET /api/quiz/next-question` - Dapatkan pertanyaan kuis random (require login)
- `POST /api/quiz/submit-answer` - Submit jawaban kuis (require login)

  Request body:
  \`\`\`json
  {
  "question_id": 1,
  "answer": "B"
  }
  \`\`\`

  Response:
  \`\`\`json
  {
  "correct": true,
  "correct_answer": "B",
  "new_score": 50
  }
  \`\`\`

## 📊 Database Schema

### Users Table

| Column      | Type        | Constraint       |
| ----------- | ----------- | ---------------- |
| id          | Integer     | PRIMARY KEY      |
| username    | String(80)  | UNIQUE, NOT NULL |
| nickname    | String(80)  | UNIQUE, NOT NULL |
| password    | String(255) | NOT NULL         |
| total_score | Integer     | DEFAULT 0        |
| created_at  | DateTime    | DEFAULT now()    |

### Quiz Questions Table

| Column         | Type        | Constraint      |
| -------------- | ----------- | --------------- |
| id             | Integer     | PRIMARY KEY     |
| topic          | String(100) | NOT NULL, INDEX |
| question       | String(500) | NOT NULL        |
| option_a       | String(255) | NOT NULL        |
| option_b       | String(255) | NOT NULL        |
| option_c       | String(255) | NOT NULL        |
| option_d       | String(255) | NOT NULL        |
| correct_answer | String(1)   | NOT NULL        |

### User Scores Table

| Column     | Type     | Constraint           |
| ---------- | -------- | -------------------- |
| id         | Integer  | PRIMARY KEY          |
| user_id    | Integer  | FOREIGN KEY, INDEX   |
| score      | Integer  | NOT NULL             |
| date_taken | DateTime | DEFAULT now(), INDEX |

## 🎓 Topik Kuis yang Tersedia

1. **AI Development**

   - Machine Learning libraries (NumPy, Scikit-learn, Pandas)
   - Natural Language Processing (NLP)
   - Deep Learning concepts
2. **Computer Vision**

   - OpenCV library
   - CNN (Convolutional Neural Networks)
   - Image recognition techniques

## 🔒 Security Features

- ✅ Password hashing dengan Werkzeug
- ✅ SQL injection prevention via ORM
- ✅ CSRF protection (Flask-Login)
- ✅ Environment variables untuk sensitive data
- ✅ SSL/TLS connection ke database
- ✅ Input validation dan sanitization

## 🐛 Troubleshooting

### Masalah Koneksi Database

\`\`\`bash

# Flush DNS cache (Windows)

ipconfig /flushdns

# Test connection

python test_connection.py
\`\`\`

### Masalah WeatherAPI

- Pastikan API key sudah valid
- Check rate limit (free tier: 1M calls/month)
- Verify internet connection

### Issues dengan Dependencies

\`\`\`bash

# Upgrade pip

pip install --upgrade pip

# Reinstall requirements

pip install -r requirements.txt --force-reinstall
\`\`\`

## 📈 Performance Optimization

- Database connection pooling (pool_size: 5)
- Query indexing pada frequently used columns
- Lazy loading relationships
- Caching weather data (bisa ditambahkan)

## 🚀 Deployment

### Deploy ke PythonAnywhere

1. Upload project ke PythonAnywhere
2. Setup virtual environment
3. Configure web app dengan WSGI
4. Set environment variables
5. Configure static files
6. Restart web app

### Deploy ke Heroku

\`\`\`bash

# Install Heroku CLI

# Login ke Heroku

heroku login

# Create app

heroku create quiz-academy-app

# Set environment variables

heroku config:set WEATHER_API_KEY=your-key
heroku config:set SECRET_KEY=your-secret

# Deploy

git push heroku main
\`\`\`

## 📝 Catatan Pengembang

- Project ini dikembangkan sebagai pembelajaran Flask web development
- Menggunakan best practices: MVC pattern, service layer, error handling
- Siap untuk production dengan beberapa konfigurasi tambahan

## 👨‍💻 Author

**Pengembang: Pael Siregar**

Untuk info lebih lanjut, lihat footer di website.

## 📜 Lisensi

Project ini open source dan dapat digunakan untuk tujuan pembelajaran dan komersial.

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk kontribusi:

1. Fork repository ini
2. Buat branch feature (\`git checkout -b feature/AmazingFeature\`)
3. Commit changes (\`git commit -m 'Add AmazingFeature'\`)
4. Push ke branch (\`git push origin feature/AmazingFeature\`)
5. Buka Pull Request

## 💬 Support

Jika ada pertanyaan atau issues:

- Buka issue di GitHub
- Hubungi developer via email

## 🎉 Terima Kasih

Terima kasih telah menggunakan Quiz Academy!

---

**Last Updated:** 2024
**Version:** 1.0.0
