import psycopg2

CONNECT_DB = {
    "host": "localhost",
    "user": "postgres",
    "password": "admin",
    "dbname": "postgres1",
    "port": "5432"
}

def init_database():
    with psycopg2.connect(**CONNECT_DB) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS tasks
                           (
                               id
                               SERIAL
                               PRIMARY
                               KEY,
                               title
                               TEXT
                               NOT
                               NULL,
                               priority
                               TEXT
                               NOT
                               NULL
                           )
                           """)
        conn.commit()