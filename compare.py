ls = [1,6]

def closestNum(numList, k): 
  diff = 0
  minDiff = 1000
  for num in range(len(numList)): 
    diff = numList[num] - k
    if (diff < 0): 
      constant = -1 
    else: 
      constant = 1
    if (constant*diff < minDiff): 
      minDiff = constant*diff
      output = numList[num]
  return (output)

def furthestNum(numList, k): 
  diff = 0
  maxDiff = 0
  for num in range(len(numList)): 
    diff = numList[num] - k
    if (diff < 0): 
      constant = -1 
    else: 
      constant = 1
    if (constant*diff > maxDiff): 
      maxDiff = constant*diff
      output = numList[num]
  return (output)

print(closestNum(ls,3))
print(furthestNum(ls,0))
