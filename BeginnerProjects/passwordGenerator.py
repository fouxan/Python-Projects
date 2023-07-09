import random
import string
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
length=int(input("How long a password do you want? "))
digs=int(input("How many digits do you want in your password? "))
symbs=int(input("How many symbols do you want in your password? "))
password=list()
rands=list()
for n in range(0,digs):
    randomNumber=random.randint(0,9)
    password.append(numbers[randomNumber])
for n in range(0,symbs):
    randomNumber=random.randint(0,8)
    password.append(symbols[randomNumber])
for n in range(0,length-digs-symbs):
    randomNumber=random.randint(0,51)
    password.append(alphabets[randomNumber])
random.shuffle(password)
print(f"{''.join(password)}")


