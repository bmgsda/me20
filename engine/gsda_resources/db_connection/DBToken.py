from base64 import urlsafe_b64encode
from hashlib import md5
from cryptography.fernet import Fernet

token = '123456789:postgres:ND90fdnd282nX'
cipher = 'gAAAAABeIk83ILi-9qp6IAzizXAPgJneAbhK55RyaSr5a8d4hrBPfLIrfm9Jwptz7dIkiCM3-znaChCWcj1ZaD2AMmPHzll-Mg=='
version = '1.0.0.0'

def get_version():
	global version
	return version

def get_token_user():
	global token
	user = token[token.find(':')+1 :]
	user = user[: user.find(':')]
	return user

def generate_key():
	global token
	token_key = md5(token.encode()).hexdigest()
	token_key64 = urlsafe_b64encode(token_key.encode())
	return token_key64

def break_cipher():
	global cipher
	key = generate_key()
	fernet_object = Fernet(key)
	pw = fernet_object.decrypt(cipher.encode())
	return pw.decode("utf-8")

def create_connection_string():
    connection_string = (
        "DRIVER={PostgreSQL Unicode};"
        "DATABASE=DB000;"
        "UID="+get_token_user()+";"
        "PWD="+break_cipher()+";"
        "SERVER=localhost;"
		"PORT=5432;"
    )
    return connection_string
