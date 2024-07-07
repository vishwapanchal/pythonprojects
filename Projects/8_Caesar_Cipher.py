import art

welcome = art.text2art("Caesar Cipher")
print(welcome)

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  shift_amount %= 26
  cipher_text = ""
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text += char
  print(f"The encoded text is {cipher_text}")

def decrypt(decode_text, decode_shift):
  decode_shift %= 26
  cipher_text = ""
  for char in decode_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position - decode_shift
      cipher_text += alphabet[new_position]
    else:
      cipher_text += char
  print(f"The decoded text is {cipher_text}")

flag = True
while flag:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == "encode":
    encrypt_text = input("Type your message:\n").lower()
    encrypt_shift = int(input("Type the shift number:\n"))
    encrypt(encrypt_text,encrypt_shift)

  elif direction == "decode":
    decode_text = input("Type your message:\n").lower()
    decode_shift = int(input("Type the shift number:\n"))
    decrypt(decode_text,decode_shift)
  else:
    print("Wrong Selection try Again!")
  
  choice = input("Do you want to continue? (y/n): ")
  if choice == "n":
    flag =  False
    print("Good bye!")

