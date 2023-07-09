import string
import random
LETTERS = list(string.ascii_letters)
DIGITS = list(string.digits)
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+']

password_l = [random.choice(LETTERS) for _ in range(random.randint(8,10))]
password_n = [random.choice(DIGITS) for _ in range(random.randint(2,4))]
password_s = [random.choice(SYMBOLS) for _ in range(random.randint(2,4))]

password_list = password_l+password_n+password_s

print(password_list)