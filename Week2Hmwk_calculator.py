# Homework for Week2 of the Python course at NMNH
# Assignment: Make a program that will perform addition, subtraction, division or multiplication of two numbers. Use appropriate error messages.

print("Welcome to the calculator!","\nPlease enter two numbers, followed by the operator to use.")

try:
	response1 = input("Enter the first number:")
	num1=float(response1)
	response2 = input("Enter the second number:")
	num2=float(response2)
except: "Please enter a valid number"
		
print("Addition=1","\nSubtraction=2","\nDivision=3","\nMultiplication=4")

while True:

	response3 = input("Please enter the number for the operator you want, when finished, enter done:")
	operator=str(response3)
	if operator=="1":
		print("The sum of ",num1,"and ",num2,"equals: ",num1+num2) 
	elif operator=="2":
		print("The difference between ",num1,"and ",num2,"equals: ",num1-num2)
	elif operator=="3":
		print("The quotient of ",num1,"and ",num2,"equals: ",num1/num2)
	elif operator=="4":
		print("The product of ",num1,"and ",num2,"equal: ",num1*num2)
	elif operator=="done":
		break
	else:
		print("Please enter a valid operator")

print("Thanks for using the calculator!")

		
	