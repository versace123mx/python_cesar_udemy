import jwt  # Not a typo
import datetime

# Your secret key, keep this secure!
secret_key = "secret_key"

# Sample payload with user information
payload = {
    "user_id": 11,
    "username": "CodersLegacy",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
}
print(datetime.datetime.utcnow())
print(datetime.timedelta(days=1))
print(datetime.datetime.utcnow() + datetime.timedelta(days=1))
# Create the JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')
print(token)
print(type(token))
#decodificacio
decodificado = jwt.decode(token,secret_key,algorithms=['HS256'])

print(decodificado)
