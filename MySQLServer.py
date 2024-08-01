import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',       # Change this to your MySQL server host
            user='your_username',   # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL statement to create the database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            # Execute the query
            cursor.execute(create_db_query)
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:  
      print("Error creating database:", err) 
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function
create_database()

