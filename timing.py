import time;
def calculate_time(func):
	'''
	prints the times it takes to run a function

	Takes note of time then runs specified function. After the function is complete,
	it will again take note of the time then print out the difference of the two times
	to give you the time it takes to run the function

	Parameters
	----------
	N/A

	Yields
	------
	Float
		The difference between the start time and ending time
	String
		Context for the Float
	'''
	def inner():
		x = time.time()
		z = func()
		y = time.time()
		print(f"Total time: {y-x}")
	return inner
def test():
	time.sleep(2)
run = calculate_time(test)
run()
