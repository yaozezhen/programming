# print ("Jane likes bunnies.")
# print (chr(65))
# print (ord("A"))
# print ("%s%d" % (chr(65), ord("A")))
# print ("%d%s" % (ord("A"), chr(65)))
name = "Jessy"
#print (name[0])

# function definitions
def add(a, b):
  return a + b
#print (add(10, 10))

def caeser_encrypt(message, code): 
  encrypted_message = []
  for letter in message: 
    # if [space], skip it
    if (letter == " "):
      encrypted_message.append(letter)
      continue
    ascii = ord(letter)
    if (ascii >= 65 and ascii <= 90): 
      case = 65
    else: 
      case = 97
    index = ord(letter) % case
    key = code % 26
    index = (index + key) % 26
    index = index + case
    encrypted_message.append(chr(index))
  return "".join(encrypted_message) 

def caeser_decrypt(message, code): 
  decrypted_message = []
  for letter in message: 
    # if [space], skip it
    if (letter == " "):
      decrypted_message.append(letter)
      continue
    ascii = ord(letter)
    if (ascii >= 65 and ascii <= 90): 
      case = 65
    else: 
      case = 97
    index = ord(letter) % case
    key = code % 26
    index = (index - key) % 26
    index = index + case
    decrypted_message.append(chr(index))
  return "".join(decrypted_message) 
 
print(caeser_encrypt("Jane is HUNGRY", 29))
# print(caeser_decrypt(caeser_encrypt("yY", 29), 29))
