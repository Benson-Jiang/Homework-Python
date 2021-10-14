import time;
def calculate_time(func):
	def inner():
		x = time.time()
		print(f"Total time {x}")
		func()
	return inner

