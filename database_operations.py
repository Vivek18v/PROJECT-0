import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': '9110786448',
    'host': 'localhost',
    'database': 'project_database'
}

def create_db():
    try:
        connection = mysql.connector.connect(
            user=config['user'],
            password=config['password'],
            host=config['host']
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(err)

# Main execution
if __name__ == "__main__":
    create_db()