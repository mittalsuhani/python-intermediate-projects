import random
password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password_length=int(input("Enter the length of the password: "))
generated_password="".join(random.sample(password,password_length))
print("Generated password: ", generated_password)

