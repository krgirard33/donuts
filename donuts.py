def donut_boxes():
  donuts = range(12)
  boxes = range(3)
  
  for box in boxes: 
      for donut in donuts:
        print("O")
      print("\n") # Creates a blank line between each box
	
donut_boxes()