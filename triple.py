def tripler(func):
	def inner():
		func()
		func()
		func()
	return inner

