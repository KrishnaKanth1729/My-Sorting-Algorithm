# A function that inverts a list

# Input: [1, 2, 4, 6, 12, 90, 104, 56, 72]
# Output: [72, 56, 104, 90, 12, 6, 4, 2, 1]

def invert_list(_list):
	length = len(_list)

	"""	if length % 2 == 0:
		is_odd = False
	else:
		is_odd  = True"""
	counter = length/2

	print(counter)

	for i in range(int(counter)):
		print(i)
		number = int(f"-{i + 1}")
		_list[i], _list[number] = _list[number]  ,_list[i]
	return _list

print(invert_list([1, 2, 4, 6, 12, 90, 104, 56, 72]))