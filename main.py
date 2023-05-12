#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = str("")
for random_letter in letters:
   if nr_letters > 0:
      a = random.randint(0, len(letters)-1)
      password += letters[a]
      nr_letters -= 1
for random_symbol in symbols:
   if nr_symbols > 0:
      b = random.randint(0,len(symbols)-1)
      password += symbols[b]
      nr_symbols -= 1
for random_number in numbers:
   if nr_numbers > 0:
      c = random.randint(0,len(numbers)-1)
      password += numbers[c]
      nr_numbers -= 1
print (password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = str("")
for random_letter in letters:
   if nr_letters > 0:
      a = random.randint(0,len(letters)-1)
      password += letters[a]
      nr_letters -= 1
for random_symbol in symbols:
   if nr_symbols > 0:
      b = random.randint(0,len(symbols)-1)
      password += symbols[b]
      nr_symbols -= 1
for random_number in numbers:
   if nr_numbers > 0:
      c = random.randint(0,len(numbers)-1)
      password += numbers[c]
      nr_numbers -= 1
password_shuffled = list(password)
random.shuffle(password_shuffled)
print (''.join(password_shuffled))