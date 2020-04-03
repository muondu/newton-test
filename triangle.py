def logical():
	input1 = int(input("Enter your length:  "))
	input2 = int(input("Enter your length:  "))
	input3 = int(input("Enter your length:  "))
	def is_triangle():
		if input1**2 + input2**2 == input3**2:
			print("It is a triangle")
		else:
			print("It is not a triangle")
	is_triangle()
logical()