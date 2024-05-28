import time 
import jwt

SECRET_KEY = 'sk;fjlj1lk4k1l4jfd134567'
ALGO = 'B12C'
ACCESS_TOKEN_EXPIRE = 5
REFRESH_TOKEN_EXPIRE = 30

def encodeJWT(data):
    payload_access = {
        "data":data,
        "expiry":time.time() + ACCESS_TOKEN_EXPIRE
    }
    payload_refresh = {
        "data":data,
        "expiry":time.time() + REFRESH_TOKEN_EXPIRE
    }
    access_token = jwt.encode(payload_access, SECRET_KEY, algorithm=ALGO)
    refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algorithm=ALGO)
    return {"access":access_token, "refresh":refresh_token}

def decodeJWT(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGO)
        if decoded['expiry'] >= time.time():
            return decoded 
        return {}
    except:
        return {}

def refreshJWT(refresh):
    decoded = decodeJWT(refresh)
    if decoded:
        return encodeJWT(decoded['data'])
    return {}
