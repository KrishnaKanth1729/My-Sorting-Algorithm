# Create a program to sort a list
# Sample Input/Output :-

# I: [1, 2, 5, 3, 10, 4]
# O: [1, 2, 3, 4, 5, 10]


def check_sort(_list):
	'''Function to check if a list is sorted.
	 Returns True or False'''
	_list = list(_list)
	k = 0
	length = len(_list)
	iteration = 0
	for item in _list:
		iteration += 1
		if iteration == length:
			break
		else:
			if _list[_list.index(item)] <= _list[_list.index(item)+1]:
				pass
			else:
				k += 1
	if k >= 1:
		return False
	else:
		return True


def sort(_list):
	res = check_sort(_list)
	list_change = [[]]
	count = 0
	if res == True:
		return f"{_list} is already sorted!"
	
	else:
			size = len(_list)
			running = True
			while running:
				for item in _list:
					
					index = _list.index(item)
					
					try:
						
						if item < _list[index + 1]:
							continue
					
						else:
							count += 1
							_list[index], _list[index + 1] = _list[index + 1], _list[index]
					
					except IndexError:
						list_change[0] = _list
						print(f"Step {int(count)}: {list_change[0]}")
						res_fin = check_sort(_list)
						if res_fin == True:
							running = False
			return f"\n\n{list_change[-1]} is the sorted list \n\n"


sample_list = [100, 200, 131, 146, 32, 78, 111]

print(sort(sample_list))

