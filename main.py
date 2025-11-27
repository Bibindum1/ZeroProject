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

def load_tasks():
    with psycopg2.connect(**CONNECT_DB) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT id, title, priority FROM tasks ORDER BY id DESC')
            tasks = cursor.fetchall()
            return tasks

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
    else:
        for task in tasks:
            print(f"{task[0]}. {task[1]} — [{task[2]}]")

def add_task():
    title = input("Введите название задачи: ")
    priority = input("Введите приоритет (Низкий/Средний/Высокий): ")
    with psycopg2.connect(**CONNECT_DB) as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO tasks (title, priority) VALUES (%s, %s)', (title, priority))
        conn.commit()
    print("Задача добавлена.")