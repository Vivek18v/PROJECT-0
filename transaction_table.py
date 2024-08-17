import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': '9110786448',
    'host': 'localhost',
    'database': 'project_database'
}

def create_transaction_logs():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Trans (
                order_id INT PRIMARY KEY,
                customer_id INT,
                product_id INT,
                product_name VARCHAR(255),
                product_category VARCHAR(255),
                payment_type VARCHAR(255),
                qty INT,
                price DECIMAL(10, 2),
                datetime DATETIME,
                ecommerce_website_name VARCHAR(255),
                payment_txn_id VARCHAR(255),
                payment_txn_success VARCHAR(50),
                failure_reason VARCHAR(255)
            )
        ''')
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        
def insert_transactionlogs(transactionlogs_dict):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Get the list of columns from the dictionary keys
        columns = list(transactionlogs_dict.keys())
        
        # Iterate over the indices of one of the columns (e.g., 'order_id')
        for index in range(len(transactionlogs_dict[columns[0]])):
            # Initialize an empty list to hold values for the current row
            values = []
            
            # Iterate over each column and append the value at the current index to the values list
            for column in columns:
                values.append(transactionlogs_dict[column][index])
            
            # Create a placeholder string for the SQL query
            placeholders = ', '.join(['%s'] * len(values))
            
            # Construct the SQL query dynamically
            sql_query = f'''
                INSERT INTO Trans ({', '.join(columns)})
                VALUES ({placeholders})
            '''
            
            # Execute the SQL query with the values list
            cursor.execute(sql_query, values)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)

# Main execution
if __name__ == "__main__":
    create_transaction_logs()