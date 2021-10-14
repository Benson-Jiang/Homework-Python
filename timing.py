import time;
def calculate_time(func):
	def inner():
		x = time.time()
		func()
		y = time.time()
		print(f"Total time{y-x}")
	return inner

