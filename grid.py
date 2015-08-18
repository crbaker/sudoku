
def block_predicates():
	predicates = dict()

	predicates[0] = lambda x, y: x < 3 and y < 3
	predicates[1] = lambda x, y: x < 3 and y >= 3 and y < 6
	predicates[2] = lambda x, y: x < 3 and y > 5

	predicates[3] = lambda x, y: x >= 3 and x < 6 and y < 3
	predicates[4] = lambda x, y: x >= 3 and x < 6 and y >= 3 and y < 6
	predicates[5] = lambda x, y: x >= 3 and x < 6 and y > 5

	predicates[6] = lambda x, y: x >= 6 and y < 3
	predicates[7] = lambda x, y: x >= 6 and y >= 3 and y < 6
	predicates[8] = lambda x, y: x >= 6 and y > 5

	return predicates

def block_for_cell(cell):
		if cell.x < 3 and cell.y < 3:
			return 0
		if cell.x < 3 and cell.y >= 3 and cell.y < 6:
			return 1
		if cell.x < 3 and cell.y > 5:
			return 2
		if cell.x >= 3 and cell.x < 6 and cell.y < 3:
			return 3
		if cell.x >= 3 and cell.x < 6 and cell.y >= 3 and cell.y < 6:
			return 4
		if cell.x >= 3 and cell.x < 6 and cell.y > 5:
			return 5
		if cell.x >= 6 and cell.y < 3:
			return 6
		if cell.x >= 6 and cell.y >= 3 and cell.y < 6:
			return 7
		if cell.x >= 6 and cell.y > 5:
			return 8

		raise ValueError("Could not determine the square for cell {0},{1}", cell.x, cell.y)
