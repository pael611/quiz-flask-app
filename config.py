import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration for SQLite local database"""
    
    # Get base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Database - SQLite Local
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(BASE_DIR, 'quiz_academy.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # API
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    
    # Database Pool - SQLite specific settings
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'timeout': 10,
            'check_same_thread': False,
        },
        'pool_pre_ping': True,
        'echo': False,
    }
    
    @classmethod
    def get_db_info(cls):
        """Return database configuration info"""
        db_path = cls.SQLALCHEMY_DATABASE_URI.replace('sqlite:///', '')
        return {
            'type': 'SQLite',
            'location': db_path,
            'environment': 'Development (Local)',
            'exists': os.path.exists(db_path),
        }

