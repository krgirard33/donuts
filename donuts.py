def donut_boxes():
  boxes = range(3)
  columns = range(4)
  rows = range(3)
  
  for box in boxes: 
      for column in columns:
        y = ''
        for row in rows: 
           y = y + "0"
        print(y) # prints the row
      print("\n") # Creates a blank line between each box
	
donut_boxes()