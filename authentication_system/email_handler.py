import smtplib
import random
import sqlite3

# Generate a random OTP
otp = random.randint(100000, 999999)

# Sender details
sender = "Private Person <from@example.com>"

# Email message template
message_template = """
Subject: Hi,
To: user,
From: {sender}
your otp: {otp}
pls do not reply
"""

def send_email(email: str):
    # Format the message with the OTP
    message = message_template.format(sender=sender, otp=otp)

    try:
        # Send the email
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
            server.starttls()
            server.login("credential1", "credential2")
            server.sendmail(sender, email, message)
            print("Email sent successfully")

        # Store the OTP in the database
        connection = sqlite3.connect("otp.db")
        cursor = connection.cursor()

        # Insert or update the OTP for the given email
        cursor.execute("""
            INSERT INTO otp_table (email, otp) VALUES (?, ?)
            ON CONFLICT(email) DO UPDATE SET otp=excluded.otp
        """, (email, otp))
        connection.commit()
        connection.close()
        print("OTP stored in the database successfully")

    except Exception as e:
        print(f"Error: {e}")

def otp_evaluator(pwd: int,email: str) -> bool:
    # Connect to the database
    connection = sqlite3.connect("otp.db")
    cursor = connection.cursor()

    # Fetch the OTP for the given email
    cursor.execute("SELECT otp FROM otp_table WHERE email = ?", (email,))
    result = cursor.fetchone()

    if result:
        stored_otp = result[0]
        if pwd == stored_otp:
            print("OTP verified successfully")
            return True
        else:
            print("Invalid OTP")
            return False
    else:
        print("Email not found in the database")
        return False
