import random 

def roll_die(n): 
  return random.randint(1,n)

def trials(n,k): 
  num_dict = {}
  for i in range(1,n+1):
    num_dict[i] = 0
  for i in range(k): 
    result = roll_die(n)
    num_dict[result] = num_dict[result] + 1
  for (key, value) in num_dict.items():
    print (str(key) + ": " + str(value) + ", probability: " + str(round(value/k*100, 2)) + "%")

def crazy_dice(n,k): 
  num_dict = {}
  for i in range(2,2*n+1):
    num_dict[i] = 0
  for i in range(k): 
    result = roll_die(n) + roll_die(n)
    num_dict[result] = num_dict[result] + 1
  print ("Roll two " + str(n) + "-sided dice " + str(k) + " times: \n")
  for (key, value) in num_dict.items():
    print ("sum of " + str(key) + ": " + str(value) + " times, probability: " + str(round(value/k*100, 2)) + "%")

def crazy_crazy_dice(x,n,k): 
  num_dict = {}
  for i in range(x,x*n+1):
    num_dict[i] = 0
  for i in range(k): 
    result = 0
    for j in range(x): 
      result += roll_die(n)
    num_dict[result] = num_dict[result] + 1
  print ("Roll " + str(x) + " " + str(n) + "-sided dice " + str(k) + " times: \n")
  for (key, value) in num_dict.items():
    print ("sum of " + str(key) + ": " + str(value) + " times, probability: " + str(round(value/k*100, 2)) + "%")

def crazy_dice_permutation(n,k): 
  num_dict = {}
  for i in range(1, n+1): 
    for j in range(1,n+1): 
      num_dict[i,j] = 0
  for i in range(k): 
    result1 = roll_die(n)
    result2 = roll_die(n)
    num_dict[result1, result2] = num_dict[result1, result2] +1
  for (key, value) in num_dict.items():
    print (str(key) + ": " + str(value) + ", probability: " + str(round(value/k*100, 2)) + "%")
