def calculator(num1, num2, operator):
	'''
	recieve input from user of two numbers and an operator and compeletes the task

	Asks user for an equation, each input seperated by a space. Depending on the operator the user gives,
	The function will either add(+), subtract(-), multiply(*), divide(/), integer division(//), or power(**). 
	If anything is invalid, it will return False

	Parameter
	---------
	num1: int
		first string inputed by user
	operator: str
		second string inputed by user
	num2: int 
		third string inputed by user
	Returns
	-------
	float
		the answer to the equation
	Example
	-------
	python3 calculator.py
	Enter equation: 10 + 11
	21
	'''
	list = ['+','-','*','/','//','**']
	for i in list:
		if operator == '+':
			return num1 + num2
		elif operator == '-':
			return num1 - num2
		elif operator == '*':
			return num1 * num2
		elif operator == '/':
			if num2 == 0:
				return False
			else:
				return num1 / num2
		elif operator == '//':
			if num2 == 0
				return False
			else:
				return num1 // num2
		elif operator == '**':
			return num1 ** num2
		else:
			return False
def parse_input():
	num1, operator, num2 = input ("Enter equation: ").split()
	return calculator(int(num1), int(num2), operator)

