def logical():
	#The first input
	input1 = int(input("Enter your length:  "))
	#The second input'
	input2 = int(input("Enter your length:  "))
	#The third input
	input3 = int(input("Enter your length:  "))
	
logical()

def is_triangle():
	#Checks if it can make a triangle
	if input1**2 + input2**2 == input3**2:
		print("It is a triangle")
	#If it cannot make a triangle
	else:
		print("It is not a triangle")
is_triangle()
