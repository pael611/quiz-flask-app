import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # Database
    SUPABASE_USER = os.environ.get('SUPABASE_USER')
    SUPABASE_PASSWORD = os.environ.get('SUPABASE_PASSWORD')
    SUPABASE_HOST = os.environ.get('SUPABASE_HOST')
    SUPABASE_PORT = os.environ.get('SUPABASE_PORT')
    SUPABASE_DBNAME = os.environ.get('SUPABASE_DBNAME')
    
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{SUPABASE_USER}:{SUPABASE_PASSWORD}@"
        f"{SUPABASE_HOST}:{SUPABASE_PORT}/{SUPABASE_DBNAME}?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # API
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    
    # Database Pool
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 5,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
        'connect_args': {
            'sslmode': 'require',
            'connect_timeout': 10,
        }
    }

