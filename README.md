# Authentication System with OTP and JWT

This project is a FastAPI-based authentication system that includes user registration, OTP-based email verification, and JWT-based authentication for secure access to protected routes. It also includes a Streamlit-based UI for user interaction.

---

## Features

1. **User Registration**:
   - Users can register with a username, password, and email.
   - Sends an OTP to the user's email for verification.

2. **OTP Verification**:
   - Users can verify their email using the OTP sent to them.

3. **Login**:
   - Users can log in with their username and password.
   - Generates a JWT token for authenticated access.

4. **Protected Routes**:
   - Access to certain routes is restricted to authenticated users with a valid JWT token.

5. **Streamlit UI**:
   - A user-friendly interface for registration, OTP verification, login, and accessing protected routes.

---

## Project Structure

```
authentication_system/
├── .env
├── api_req_otp.py
├── api_request.py
├── db_cr.py
├── email_handler.py
├── jwt_handler.py
├── main.py
├── otp.db
├── streamlit_app.py
├── users.db
```

---

## Prerequisites

- Python 3.10 or higher
- SQLite (for user and OTP storage)
- Mailtrap account for email functionality

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/authentication_system.git
   cd authentication_system
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the `authentication_system` directory.
   - Add the following variables:
     ```
     SECRET=<your_jwt_secret_key>
     ALGORITHM=HS256
     s_l=<your_custom_value>
     ```

5. **Configure Email Credentials**:
   - Open `email_handler.py` and replace the placeholders `"credential1"` and `"credential2"` with your actual Mailtrap credentials:
     ```python
     server.login("your_mailtrap_username", "your_mailtrap_password")
     ```

---

## Usage

1. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Streamlit UI**:
   - Run the Streamlit app:
     ```bash
     streamlit run streamlit_app.py
     ```
   - Open the URL provided by Streamlit in your browser.

3. **API Endpoints**:
   - **Register**: `POST /register`
   - **Verify OTP**: `POST /otp`
   - **Login**: `POST /login`
   - **Protected Route**: `POST /protected`

---

## Example API Requests

### 1. **Register User**
Endpoint: `POST /register`

```bash
curl -X POST http://127.0.0.1:8000/register \
-H "Content-Type: application/json" \
-d '{
  "name": "testuser",
  "pwd": "password123",
  "email": "testuser@example.com"
}'
```

### 2. **Verify OTP**
Endpoint: `POST /otp`

```bash
curl -X POST http://127.0.0.1:8000/otp \
-H "Content-Type: application/json" \
-d '{
  "otp": 123456,
  "email": "testuser@example.com"
}'
```

### 3. **Login**
Endpoint: `POST /login`

```bash
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser",
  "password": "password123"
}'
```

### 4. **Access Protected Route**
Endpoint: `POST /protected`

```bash
curl -X POST http://127.0.0.1:8000/protected \
-H "Authorization: Bearer <your_jwt_token>"
```

Replace `<your_jwt_token>` with the token received from the login response.

---

## Configuration

### Email Settings
- Update the SMTP server and port in `email_handler.py` if you're using a different email provider:
  ```python
  with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
  ```

### JWT Settings
- Update the `SECRET_KEY` and `ALGORITHM` in the `.env` file for secure token generation.

---

## Dependencies

- `fastapi`
- `sqlite3`
- `pydantic`
- `python-decouple`
- `streamlit`
- `requests`

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **FastAPI**: For building the backend.
- **Streamlit**: For creating the user interface.
- **Mailtrap**: For email testing and delivery.
