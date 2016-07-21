# Homework for Week1 Python course at NMNH
# 
# Make a program to add a series of numbers
# Ask for the user to input a series of numbers, then add the numbers and give the result

nums=list()

while True:
	try: 
		num = input("Enter a number to add. When finished, enter done: ")
		if num == "done": break
		else: 
			value = float(num)
			nums.append(value)
	except: "Please enter a valid number"

print("The sum is: ",sum(nums))