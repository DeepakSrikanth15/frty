username_db="Admin"
password_db="1234"

username = input("Enter usernmae:")
password = input("Enter password:")
if username == username_db and password == password_db:
    print("Login Successful")
else:
    print("unsuccesful")