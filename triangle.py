def logical():
	#The first input
	global input1
	input1 = int(input("Enter your length:  "))
	#The second input'
	global input2
	input2 = int(input("Enter your length:  "))
	#The third input
	global input3
	input3 = int(input("Enter your length:  "))
	
logical()

global input2
global input3
def is_triangle():
	#Checks if it can make a triangle
	if input1**2 + input2**2 == input3**2:
		print("It is a triangle")
	#If it cannot make a triangle
	else:
		print("It is not a triangle")
is_triangle()
