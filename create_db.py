"""
Manual database creation script
Jalankan ini jika ingin membuat database secara manual
"""
import os
import sys
import logging

# Setup logging before importing app
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('create_db.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

try:
    from app import app, db, init_db
except ImportError as e:
    logger.error(f"Failed to import app: {e}")
    print("❌ ERROR: Could not import app module")
    sys.exit(1)

print("=" * 70)
print("QUIZ ACADEMY - DATABASE CREATION SCRIPT")
print("=" * 70)

try:
    print("\n[1] Checking database file...")
    from config import Config
    
    db_info = Config.get_db_info()
    db_path = db_info['location']
    
    print(f"  Database Type: {db_info['type']}")
    print(f"  Database Location: {db_path}")
    print(f"  Database Exists: {db_info['exists']}")
    
    if db_info['exists']:
        try:
            file_size = os.path.getsize(db_path)
            print(f"  File Size: {file_size} bytes")
        except Exception as e:
            print(f"  ⚠️  Could not get file size: {e}")
    
    print("\n[2] Creating database...")
    init_db()
    
    print("\n[3] Verifying database...")
    from sqlalchemy import inspect
    
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    
    print(f"\n  ✅ Database created successfully!")
    print(f"  Tables created: {len(tables)}")
    for table in tables:
        columns = inspector.get_columns(table)
        print(f"    - {table} ({len(columns)} columns)")
    
    print("\n" + "=" * 70)
    print("✅ DATABASE CREATION COMPLETE")
    print("=" * 70)
    
    if os.path.exists(db_path):
        try:
            file_size = os.path.getsize(db_path)
            print(f"\nDatabase file: {db_path}")
            print(f"File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            logger.info(f"Database created successfully at {db_path}")
        except Exception as e:
            print(f"\n⚠️  Could not get file info: {e}")
    
except Exception as e:
    print(f"\n❌ DATABASE CREATION FAILED")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    logger.error(f"Database creation failed: {e}", exc_info=True)
    sys.exit(1)
