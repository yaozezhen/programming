import random

def nineNum(): 
  numList = []
  while len(numList) < 9: 
    num = random.randint(1,9)
    if num not in numList: 
      numList.append(num)
  return numList

print(nineNum())
