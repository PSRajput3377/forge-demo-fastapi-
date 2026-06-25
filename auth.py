import jwt

def verify(token):
    return jwt.decode(token, 'secret', algorithms=['HS256'])
