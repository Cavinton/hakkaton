import time
from jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email": "qwerty123@mail.ru", "username": "Kulik", "id": 1}

jwt_token = encodeJWT(user) # {"access_token":adadfdgwer, "refresh_token":asdf213h23hr23}
print(jwt_token)

#остановка кода на 6cек
time.sleep(6)

#прилетает декодированный токен, если время не истекло, если время жизни токена истекло, прилетает пустой dict
decoded = decodeJWT(jwt_token['access'])
print(decoded)

#$ обновляет старые токены на новые
new_jwt_token = refreshJWT(jwt_token['refresh'])
print(new_jwt_token)