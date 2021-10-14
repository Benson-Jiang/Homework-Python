def swap_last_item(x):
	'''
	Take a list and swap the first and last item
	Saves the first and last item from a list of ints then removes the first and last items and replaces them flipped.
	Parameters
	--------
	x: list of int
		list of numbers you want to swap
	first: int
		first integer of the list
	last: int
		last integer of the list
	Returns
	--------
	x: list of int
		List with swapped first and last item
	Example
	--------
	>>x = [12,35,5,9,56,24]
	>>swap_last_item(x)
	[24,35,5,9,56,12]
	'''
	length = len(x)
	if length <= 1:
		return x
	else:
		first = x[0]
		last = x[length - 1]
		x.pop(0)
		x.insert(0,last)
		x.pop(length - 1)
		x.append(first)
		return x

