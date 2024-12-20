import mysql.connector

pas = ""

# Connection settings
# DB_CONFIG = {
#     "host": "localhost",
#     "user": "root",
#     "password": pas,
#     "database": "demodata"
# }

def connect_db():
    # return mysql.connector.connect(**DB_CONFIG)
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=pas,
        database="calories",
        allow_local_infile=True
    )

def setup_database():
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        );
        """)

        print("users table created succefully.")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            height INT NOT NULL,
            weight INT NOT NULL,
            workout_duration INT NOT NULL
        );
        """)

        print("data_table table created succefully.")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            height INT NOT NULL,
            weight INT NOT NULL,
            workout_duration INT NOT NULL, 
            
        );
        """)

        print("final_data table created succefully.")
        
        db.commit()
        db.close()
    except Exception as e:
        print(f"Database setup failed: {e}")


def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pas
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS calories;")
    print("Database created successfully")
    setup_database()
    mydb.commit()
    mydb.close()
