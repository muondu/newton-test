def logical():
	input1 = int(input("Enter your first length:  "))
	input2 = int(input("Enter your second length:  "))
	input3 = int(input("Enter your third length:  "))
logical()
def is_triangle(a,b,c):
	if a + b > c and b + c > a and a + c > b:
		print("It is a triangle")
	else:
		print("It is not a triangle")
is_triangle(input1,input2,input3)
