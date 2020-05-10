import math

def regPolygonArea(n, k): 
  interiorAngle = ((n - 2) * 180 / n) * math.pi / 180
  baseAngle = interiorAngle / 2
  height = math.tan(baseAngle) * (k / 2)
  triArea = height * k / 2
  polyArea = triArea * n
  print("The area of a regular " + str(n) + "-sided polygon wth side length " + str(k) + " is: " + str(round(polyArea, 2)) + ". ")

regPolygonArea(3,4)

