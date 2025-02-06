import random
import string
desired_length = int(input("Enter the desired length of the password: "))
password =''
for i in range(desired_length):
    password +=random.choice(string.ascii_letters + string.digits + string.punctuation)

print("Generated Password = ",password)