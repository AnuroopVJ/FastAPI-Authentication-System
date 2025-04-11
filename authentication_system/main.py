from typing import Union

import jwt
import datetime
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time

from jwt_handler import signJWT, decodeJWT
from email_handler import send_email, otp_evaluator

connection = sqlite3.connect("users.db", check_same_thread=False)
print(connection.total_changes)
app = FastAPI()
cursor = connection.cursor()


regi_login = int

class user(BaseModel):
    name: str
    pwd: str
    email: str

class LoginRequest(BaseModel):
    username: str
    password: str

class OTP(BaseModel):
    otp: int
    email: str

def email_exists(email):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def read_users():

    cursor.execute("SELECT username, password FROM users")
    users = cursor.fetchall()

    for i in users:
        print(i)

@app.get("/")
def read_root():
    return {"Please Pass information","username and password"}

@app.post("/register")
def register_user(user: user):
    username = user.name
    password = user.pwd
    email = user.email 

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE usern = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return {"message": "Username already exists"}
    
    # Check if the email already exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_email = cursor.fetchone()

    if existing_email:
        return {"message": "Email already exists"}

    # Insert new user into the database
    if existing_email==None and existing_user==None:
        cursor.execute("INSERT INTO users (usern, pwd, email) VALUES (?, ?, ?)", (username, password, email))
        connection.commit()
        send_email(email)
        return {"message": "User registered successfully, OTP sent to email"}

@app.post("/otp")
def get_otp(data: OTP):
    otp = data.otp
    email = data.email

    if otp_evaluator(otp,email) == True:
        return {"message": "OTP verified Successfully"},{"login":"Succesful"}

    else:
        return {"message": "Invalid OTP"}


@app.post("/login")
def login(data: LoginRequest):
    username = data.username
    password = data.password

    cursor.execute("SELECT * FROM users WHERE usern = ? AND pwd = ?", (username, password))
    result = cursor.fetchone()  # Fetch one matching record
    if result is None:
        return {"message": "Invalid username or password"}
    else:
        token = signJWT(username)
        return {"access token": token, "username": username, "password": password}

    

@app.post("/protected")
def protected_route(request: Request):
    token = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        payload = decodeJWT(token)
        return {"message": "Protected route accessed", "payload": payload}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")