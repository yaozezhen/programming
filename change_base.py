def binary_to_decimal(s): 
  flip_s = list(reversed(str(s)))
  decimal = 0 
  count = 0
  for num in flip_s: 
    decimal += int(num) * (2 ** count)
    count += 1
  return decimal

def decimal_to_binary(s): 
  binary = []
  num = int(s)
  while (num > 0):
    binary.append(str(int(num) % 2))
    num = int(num / 2)
  binary = list(reversed(binary))
  return "".join(binary)

#print (binary_to_decimal("1100100"))
#print (decimal_to_binary(100))

def base_to_decimal(s,b): 
  flip_s = list(reversed(str(s)))
  decimal = 0 
  count = 0
  for num in flip_s: 
    real_num = num
    if ord(real_num) > 64: 
      real_num = str((ord(real_num)) - 65 + 10)
    decimal += int(real_num) * (b ** count)
    count += 1
  return decimal

def decimal_to_base(s,b): 
  base = []
  num = int(s)
  while (num > 0):
    if ((num % b) > 9): 
      digit = chr((num % b) + 65 - 10)
    else: 
      digit = str(int(num % b))
    base.append(digit)
    num = int(num / b)
  base = list(reversed(base))
  return "".join(base)

print (base_to_decimal("29A",16))
print (decimal_to_base(666,16))
