import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': '9110786448',
    'host': 'localhost',
    'database': 'project_database'
}

def create_customerstable():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cust (
                customer_id INT PRIMARY KEY,
                customer_name VARCHAR(255),
                country VARCHAR(255),
                city VARCHAR(255)
            )
        ''')
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)

def insert_customers(customers_dict):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        columns = list(customers_dict.keys())
        
        for index in range(len(customers_dict[columns[0]])):
            values = [customers_dict[column][index] for column in columns]
            placeholders = ', '.join(['%s'] * len(values))
            
            sql_query = f'''
                INSERT INTO Cust ({', '.join(columns)})
                VALUES ({placeholders})
            '''
            
            cursor.execute(sql_query, values)
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)

# Main execution
if __name__ == "__main__":
    create_customerstable()