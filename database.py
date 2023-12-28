from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

url = os.getenv("DATABASE_URL")

connection = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
)

def connect():
    # Connect to PostgreSQL
    postgresql_connection = connection
    try:
        if postgresql_connection:
            # create cursor
            cursor = postgresql_connection.cursor()
            # exectute test statement
            cursor.execute('SELECT version()')
            
            
            # display version and connection
            return {
                "PostgreSQL": cursor.fetchone(),
                "Connection": "Connected to PostgreSQL DB..."
            }, cursor.close() # close communication with PostgreSQL
            

    except (Exception, psycopg2.DatabaseError) as e:
        return {
            "Error Message": str(e)
        }
    
def disconnect():
    print("Disconnecting from the database...")
    global connection  # Use the global keyword to access the module-level variable

    try:
        if connection is not None and connection.closed == 0:
            connection.close()
            print("Database connection closed.")
        else:
            print("No active database connection to close.")
    except Exception as e:
        print("Error while disconnecting:", str(e))