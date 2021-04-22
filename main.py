# Create a program to sort a list
# Bonus: Use a function to check if the list is sorted
# Sample Input/Output :-
# I: [1, 2, 5, 3, 10, 4]
# O: [1, 2, 3, 4, 5, 10]


def check_sort(_list):
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
		return f"list is already sorted!"
	
	else:
			size = len(_list)
			running = True
			while running:
				for item in _list:
					count += 1
					index = _list.index(item)
					
					try:
						
						if item < _list[index + 1]:
							continue
					
						else:
							_list[index], _list[index + 1] = _list[index + 1], _list[index]
					
					except IndexError:
						list_change[0] = _list
						print(f"Step {int(count/10)}: {list_change[0]}")
						res_fin = check_sort(_list)
						if res_fin == True:
							running = False
			return f"\n\n{list_change[-1]} is the sorted list \n\n"


sample_list = [1, 3, 4, 5, 9, 0, 12, 4, 5, 7]

print(sort(sample_list))

