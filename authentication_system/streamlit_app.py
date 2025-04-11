import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Auth System", layout="centered")

st.title("🔐 Auth System UI")

# Session state to store token
if "token" not in st.session_state:
    st.session_state.token = None

# Navigation
page = st.sidebar.selectbox("Navigate", ["Register", "Verify OTP", "Login", "Protected Route"])

# Register Page
if page == "Register":
    st.subheader("📩 Register User")

    name = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    email = st.text_input("Email")

    if st.button("Register"):
        payload = {"name": name, "pwd": pwd, "email": email}
        res = requests.post(f"{API_BASE_URL}/register", json=payload)

        if res.status_code == 200:
            st.success(res.json().get("message"))
        else:
            st.error("Registration failed")

# OTP Page
elif page == "Verify OTP":
    st.subheader("\u2705 Verify OTP")
    otp = st.number_input("Enter OTP", step=1)
    email = st.text_input("Email")

    if st.button("Verify"):
        payload = {"otp": otp, "email": email}
        res = requests.post(f"{API_BASE_URL}/otp", json=payload)

        if res.status_code == 200:
            for msg in res.json():
                st.success(msg)
        else:
            st.error("Invalid OTP or error verifying")

# Login Page
elif page == "Login":
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        payload = {"username": username, "password": password}
        res = requests.post(f"{API_BASE_URL}/login", json=payload)
        data = res.json()

        if res.status_code == 200 and "access token" in data:
            st.session_state.token = data["access token"]
            st.success("Login successful")
            st.code(data)
        else:
            st.error(data.get("message", "Login failed."))

# Protected Route
elif page == "Protected Route":
    st.subheader("🛡️ Protected Route")

    if st.session_state.token:
        headers = {"Authorization": st.session_state.token}
        res = requests.post(f"{API_BASE_URL}/protected", headers=headers)

        if res.status_code == 200:
            st.success("Access granted")
            st.json(res.json())
        else:
            st.error("Access denied: Invalid or expired token")
    else:
        st.warning("Please login first to access protected route.")
