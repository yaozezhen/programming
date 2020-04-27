def mobius_pattern(n): 
  if n % 2 == 0: 
    side_piece = 2
    twist_after_cutting = n
  if n % 2 == 1: 
    side_piece = 1
    twist_after_cutting = 2*n + 2
  print("A " + str(n) + "-twisted Mobius strip will have: \n \n" + str(side_piece) + " sides, " + str(side_piece) + " pieces after cutting, and " + str(twist_after_cutting) + " twists after cutting.")

mobius_pattern(99)
