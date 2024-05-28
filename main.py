import time
from jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email": "qwerty123@mail.ru", "username": "Kulik", "id": 1}

jwt_token = encodeJWT(user) 
print(jwt_token)

time.sleep(6)

decoded = decodeJWT(jwt_token['access'])
print(decoded)

new_jwt_token = refreshJWT(jwt_token['refresh'])
print(new_jwt_token)