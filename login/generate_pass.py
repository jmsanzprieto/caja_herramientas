import bcrypt

password = "ABC1234".encode('utf-8')
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
print(hashed_password)