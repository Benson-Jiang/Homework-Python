def tripler(func):
	'''
	runs the given function 3 times
	'''
	def inner():
		func()
		func()
		func()
	return inner

