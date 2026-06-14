import os
import sys
import django
from pathlib import Path

# Setup paths for django imports
base_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(base_dir / 'backend' / 'src'))
sys.path.insert(0, str(base_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

def clean_seats():
    with connection.cursor() as cursor:
        # Update any non-numeric seats to a default value, or extract the first digit
        # PostgreSQL syntax
        cursor.execute("""
            UPDATE core_vehicle 
            SET seats = 4 
            WHERE seats::text NOT SIMILAR TO '^[0-9]+$'
        """)
        print("Cleaned up non-numeric seats.")

if __name__ == '__main__':
    clean_seats()
