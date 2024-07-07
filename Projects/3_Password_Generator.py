import random as rd

print("Welcome to password generator")

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%',"(",")","*","&","+","- "]

pass_chars = int(input("How many lettters you want in your password? : "))
pass_numbers = int(input("How many numbers you want in your password? : "))
pass_symbols = int(input("how many symbols you want in your password? : "))

password = []

for i in range(0,pass_chars):
    password.append(rd.choice(chars))

for i in range(0,pass_numbers):
    password.append(rd.choice(numbers))

for i in range(0,pass_symbols):
    password.append(rd.choice(symbols))

rd.shuffle(password)
generated_password = ""
for i in password:
    generated_password+= i
    
print(generated_password)
    
