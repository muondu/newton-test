input1 = int(input("Enter your first length of a triangle:  "))
input2 = int(input("Enter your second length of a triangle:  "))
input3 = int(input("Enter your thiird length of a triangle:  "))
def is_triangle():
	if input1 == input2 and input3:
		print("Yes")
	else:
		print("NO")
		
is_triangle()