import psycopg2

try:
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_username',
        password='your_password',
        host='your_host',
        port='your_port'
    )
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
