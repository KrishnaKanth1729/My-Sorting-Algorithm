def get_elements(equation):
	equation = str(equation)
	LOW_ALPHA = ['a', 'b', 'x', 'y', 'p']
	HIGH_ALPHAS = [item.upper() for item in LOW_ALPHA]
	OPERATORS = ['+', '-', '*', '/']
	SYMBOLS = ['(', ')', '^']

	operators = []
	for item in operators:
		if item in equation:
			operators.append(item)
	


get_elements('x + y / ( 2 ^ 2 )')