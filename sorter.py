numbers = [1, 2, 3, 4]
def get_max(_list):
	max_el_count = 0
	for item in _list:
		for _item in _list:
			if item >= _item:
				max_el_count += 1

		if max_el_count == len(_list):
			if _list.count(item) > 1:
				num = []
				for i in range(_list.count(item)):
					num.append(item)
				return num

			else:
				return item

		else:
			max_el_count = 0
			continue


print(get_max([1, 2, 3, 4, 5, 6, 10, 56, 100, 91, 200, 151]))
