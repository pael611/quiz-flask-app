from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv
import os
import sys
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

print("=" * 60)
print("SQLITE LOCAL DATABASE CONNECTION TEST")
print("=" * 60)

# Get database path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'quiz_academy.db')

print("\n[1] Verifying Database Configuration:")
print(f"  Database Type: SQLite (Local)")
print(f"  Database Path: {DB_PATH}")
logger.info(f"Testing database at: {DB_PATH}")

# Step 2: Test database creation/connection
print("\n[2] Testing SQLAlchemy Connection:")
try:
    DATABASE_URL = f"sqlite:///{DB_PATH}"
    engine = create_engine(
        DATABASE_URL,
        connect_args={'check_same_thread': False, 'timeout': 10},
        echo=False
    )
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1 as connection_test"))
        row = result.fetchone()
        print(f"  ✅ SQLAlchemy connection successful!")
        print(f"  → Query result: {row}")
        logger.info("✅ Database connection successful")
        
except Exception as e:
    print(f"  ❌ Connection failed!")
    print(f"  → Error: {e}")
    logger.error(f"Connection failed: {e}", exc_info=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 3: Test database query
print("\n[3] Testing Database Query:")
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT sqlite_version()"))
        version = result.fetchone()[0]
        print(f"  ✅ SQLite version: {version}")
        logger.info(f"SQLite version: {version}")
except Exception as e:
    print(f"  ❌ Query failed: {e}")
    logger.error(f"Query failed: {e}", exc_info=True)
    sys.exit(1)

# Step 4: Check existing tables
print("\n[4] Checking Database Tables:")
try:
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if tables:
        print(f"  ✅ Found {len(tables)} existing tables:")
        for table in tables:
            print(f"    - {table}")
        logger.info(f"Found {len(tables)} tables: {', '.join(tables)}")
    else:
        print(f"  ℹ️  No tables found (database will be created on first run)")
        logger.info("No tables found - database will be initialized on first run")
except Exception as e:
    print(f"  ⚠️  Error checking tables: {e}")
    logger.warning(f"Error checking tables: {e}")

# Step 5: Check database file
print("\n[5] Database File Status:")
if os.path.exists(DB_PATH):
    try:
        file_size = os.path.getsize(DB_PATH)
        print(f"  ✅ Database file exists")
        print(f"  → File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
        logger.info(f"Database file exists - size: {file_size} bytes")
    except Exception as e:
        print(f"  ⚠️  Error getting file size: {e}")
        logger.warning(f"Error getting file size: {e}")
else:
    print(f"  ℹ️  Database file does not exist yet")
    print(f"  → Will be created on app initialization")
    logger.info("Database file will be created on initialization")

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED - LOCAL DATABASE READY!")
print("=" * 60)
logger.info("✅ All tests passed - database ready")
