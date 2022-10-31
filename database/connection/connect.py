import psycopg2
from .config import config

def connect():
    """Connect to postgres football database"""
    conn = None
    try:
        params = config()

        print('Connection to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        print('Success!')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1

    return conn