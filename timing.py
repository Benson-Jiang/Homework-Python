import time;
def calculate_time(func):
	def inner():
		x = time.time()
		z = func()
		y = time.time()
		print(f"Total time{y-x}")
		return z
	return inner
def test():
	time.sleep(2)
run = calculate_time(test)
run()
