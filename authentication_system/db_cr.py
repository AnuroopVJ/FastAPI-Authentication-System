import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("otp.db")
cursor = connection.cursor()

# Create the table if it doesn't exist
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS otp_db (
        email TEXT NOT NULL,
        otp TEXT NOT NULL
    )
    """)
    connection.commit()
    print("Database and table 'otp_db' created successfully.")
except sqlite3.Error as e:
    print(f"Error creating the table: {e}")

# Close the connection
connection.close()