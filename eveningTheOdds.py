import random 

die_1 = [1, 2, 3, 4]
die_2 = [1, 1, 1, 1, 1]
die_3 = [1, 2, 3, 4, 5, 6]

def eveningTheOdds(diceList,k): 
  die1 = diceList[0]
  die2 = diceList[1]
  sumDict = {}
  for i in range(max(die1) + max(die2) + 1): 
    sumDict[i] = 0
  for i in range(k): 
    outcome = random.choice(die1) + random.choice(die2)
    sumDict[outcome] += 1
  for (key, value) in sorted(sumDict.items()): 
    if (value > 0): 
      print ("sum of", str(key) + ":", value, "times, probability:", str(round(int(value)/k*100, 2)) + "%")

#eveningTheOdds([die_1, die_2], 10000)

def permutationETO(diceList,k): 
  die1 = diceList[0]
  die2 = diceList[1]
  sumDict = {}
  for i in range(max(die1) + 1): 
    for j in range(max(die2) + 1): 
      sumDict[i,j] = 0
  for i in range(k): 
    outcome1 = random.choice(die1)
    outcome2 = random.choice(die2)
    sumDict[outcome1, outcome2] += 1
  for (key, value) in sumDict.items(): 
    if (value > 1): 
      print ("sum of", str(key) + ":", value, "times, probability:", str(round(value/k*100, 2)) + "%")

#permutationETO([die_1, die_2], 10000)

def crazyETO(diceList,k): 
  maxSum = 0
  sumDict = {}
  for i in range(len(diceList)): 
    maxSum += max(diceList[i])
  for i in range(maxSum + 1): 
    sumDict[i] = 0
  for i in range(k): 
    outcome = 0
    for j in range(len(diceList)): 
      outcome += random.choice(diceList[j])
    sumDict[outcome] += 1
  for (key, value) in sorted(sumDict.items()): 
    if (value > 0): 
      print ("sum of", str(key) + ":", value, "times, probability:", str(round(int(value)/k*100, 2)) + "%")

crazyETO([die_1, die_2, die_3], 10000)
