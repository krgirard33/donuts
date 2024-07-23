def donut_boxes():
  donuts = int(input("Enter the number of donuts: "))
  
  # Calculate total donuts, including extra
  total_donuts = donuts + donuts // 12
  
  box_number = 1
  while total_donuts > 0:
    print(f"Box {box_number}")
    donuts_in_box = min(12, total_donuts)
    total_donuts -= donuts_in_box
        
    for row in range(4): 
      for column in range(3):
        if donuts_in_box > 0:
          print("O", end="")
          donuts_in_box -= 1
        else:
          print(" ", end="")
      print()
    print()
    box_number += 1
	
donut_boxes()