import time
import jwt
from decouple import config


JWT_SECRET_KEY = config("SECRET_KEY")
JWT_ALGORITHM = config("ALGORITHM")

def signJWT(userid: str):
    payload = {
        'sub': userid,  # JWT best practice
        'exp': int(time.time()) + 3600
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        print("Decoded token:", decode_token)
        return decode_token if decode_token['exp'] >= int(time.time()) else None
    except:
        return None

