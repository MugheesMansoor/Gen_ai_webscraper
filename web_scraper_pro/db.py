import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # your XAMPP MySQL username
        password="",        # your XAMPP MySQL password (empty by default)
        database="scraped_jobs"
    )
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Table already created, so this is optional
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fake_jobs(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        company VARCHAR(255),
        location TEXT,
        link VARCHAR(50),
        discription TEXT
    )
    """)

    conn.commit()
    conn.close()