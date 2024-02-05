from jose import jwt
import time,datetime

secreto = '123456'
ts = int(time.time())
payload = {
    "user_id": 11,
    "username": "CodersLegacy",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
}

token = jwt.encode(payload,secreto,algorithm='HS256')
print(type(token))