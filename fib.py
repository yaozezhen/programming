def fib (message, n): 
  if n < 1: 
    print ("nah")
    return
  num1 = 1
  print (message)
  if n == 1: 
    return
  num2 = 1
  print (message)
  current = 0
  for i in range (3, n+1): 
    current = num1 + num2 
    new_mess = ""
    for j in range (0, current): 
      new_mess = new_mess + message + " "
    print (new_mess)
    num1 = num2
    num2 = current
  return 

fib ("pa", 5)
