def strLenVar(strList): 
  lenSum = 0
  lenList = len(strList)
  sqrdDiffSum = 0
  for item in strList: 
    lenSum += len(item)
  lenMean = lenSum / lenList
  for item in strList: 
    sqrdDiffSum += ((len(item) - lenMean) ** 2)
  var = sqrdDiffSum / lenList
  print (var)

strLenVar(["cat", "hello", "screen", "tessellation"])
