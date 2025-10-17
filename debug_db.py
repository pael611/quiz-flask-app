"""
SQLite database debugging script
"""
import os
import sys
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

print("=" * 70)
print("SQLITE LOCAL DATABASE DEBUG SCRIPT")
print("=" * 70)

# Get database path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'quiz_academy.db')

# Step 1: Check database file
print("\n[1] Database File Status:")
if os.path.exists(DB_PATH):
    try:
        file_size = os.path.getsize(DB_PATH)
        print(f"  ✅ Database file exists")
        print(f"  → Location: {DB_PATH}")
        print(f"  → Size: {file_size} bytes ({file_size / 1024:.2f} KB)")
        logger.info(f"Database file found: {DB_PATH} ({file_size} bytes)")
    except Exception as e:
        print(f"  ⚠️  Error getting file size: {e}")
        logger.warning(f"Error getting file size: {e}")
else:
    print(f"  ℹ️  Database file does not exist yet")
    print(f"  → Will be created: {DB_PATH}")
    logger.info("Database file will be created on initialization")

# Step 2: Build connection string
print("\n[2] Building Connection String:")
try:
    from config import Config
    db_uri = Config.SQLALCHEMY_DATABASE_URI
    print(f"  ✅ URI: {db_uri}")
    logger.info(f"Database URI: {db_uri}")
except Exception as e:
    print(f"  ❌ Error: {e}")
    logger.error(f"Error building connection string: {e}")
    sys.exit(1)

# Step 3: Test connection
print("\n[3] Testing SQLite Connection:")
try:
    engine = create_engine(db_uri, echo=False)
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"  ✅ Connection successful")
        
        # Get SQLite info
        result = connection.execute(text("SELECT sqlite_version()"))
        version = result.fetchone()[0]
        print(f"  ✅ SQLite version: {version}")
        logger.info(f"✅ Connection successful - SQLite {version}")
        
except Exception as e:
    print(f"  ❌ Connection failed: {e}")
    logger.error(f"Connection failed: {e}", exc_info=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 4: Check tables
print("\n[4] Checking Database Tables:")
try:
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if tables:
        print(f"  ✅ Found {len(tables)} tables:")
        for table in tables:
            columns = inspector.get_columns(table)
            print(f"    - {table} ({len(columns)} columns)")
        logger.info(f"Found {len(tables)} tables")
    else:
        print(f"  ℹ️  No tables found (empty database)")
        logger.info("No tables found - database is empty")
        
except Exception as e:
    print(f"  ❌ Error checking tables: {e}")
    logger.error(f"Error checking tables: {e}")

# Step 5: Check data
print("\n[5] Checking Data in Tables:")
try:
    with engine.connect() as connection:
        tables_to_check = ['user', 'quiz_question', 'user_score']
        
        for table in tables_to_check:
            try:
                result = connection.execute(text(f"SELECT COUNT(*) FROM `{table}`"))
                count = result.fetchone()[0]
                print(f"  ✅ {table}: {count} rows")
                logger.info(f"{table}: {count} rows")
            except Exception as e:
                print(f"  ⚠️  {table}: Table does not exist or error")
                logger.warning(f"{table}: {str(e)[:50]}")
                
except Exception as e:
    print(f"  ❌ Error checking data: {e}")
    logger.error(f"Error checking data: {e}")

# Step 6: Get database info
print("\n[6] Database Configuration:")
db_info = Config.get_db_info()
for key, value in db_info.items():
    print(f"  {key}: {value}")
    logger.info(f"{key}: {value}")

print("\n" + "=" * 70)
print("✅ DEBUG COMPLETE")
print("=" * 70)
logger.info("✅ Debug complete")
