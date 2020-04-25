import random 

def caesar_encrypt(message, code): 
  encrypted_message = []
  for letter in message: 
    ascii_l = ord(letter)
    if (ascii_l < 65 or (ascii_l < 97 and ascii_l > 90) or ascii_l > 122):
      encrypted_message.append(letter)
      continue
    if (ascii_l >= 65 and ascii_l <= 90): 
      case = 65
    else: 
      case = 97
    index = ascii_l % case
    key = code % 26
    index = (index + key) % 26
    index = index + case
    encrypted_message.append(chr(index))
  return "".join(encrypted_message) 

def caesar_decrypt(message, code): 
  decrypted_message = []
  for letter in message: 
    ascii_l = ord(letter)
    if (ascii_l < 65 or (ascii_l < 97 and ascii_l > 90) or ascii_l > 122):
      decrypted_message.append(letter)
      continue
    if (ascii_l >= 65 and ascii_l <= 90): 
      case = 65
    else: 
      case = 97
    index = ascii_l % case
    key = code % 26
    index = (index - key) % 26
    index = index + case
    decrypted_message.append(chr(index))
  return "".join(decrypted_message) 
 
def crazy_caesar_encrypt(message, key): 
  encrypted_message = []
  i = 0
  for letter in message: 
    encrypted_message.append(caesar_encrypt(letter, key[i % len(key)]))
    i = i + 1
  return "".join(encrypted_message)

def crazy_caesar_decrypt(message, key): 
  decrypted_message = []
  i = 0
  for letter in message: 
    decrypted_message.append(caesar_decrypt(letter, key[i % len(key)]))
    i = i + 1
  return "".join(decrypted_message)

def enigma(message): 
  key = []
  for letter in message: 
    randkey = random.randint(-1000, 1000)
    key.append(randkey)
  print (crazy_caesar_encrypt(message, key))
  print (crazy_caesar_decrypt(crazy_caesar_encrypt(message, key), key))

enigma("Hello, world!")
