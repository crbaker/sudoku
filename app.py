from cell import Cell
from file_utils import FileReader

class Game:

	def __init__(self, file_name):
		self.grid = self.read_grid(file_name)

	def read_grid(self, file_name):
		reader = FileReader(file_name)
		return reader.build_grid()

	def solve_grid(self):
		groups = []

		for i in range(9):
			groups.append(self.group_cells(lambda c: c.in_block(i)))
			groups.append(self.group_cells(lambda c: c.in_row(i)))
			groups.append(self.group_cells(lambda c: c.in_column(i)))

		for group in groups:
			for number in range(1, 10):
				self.place_possible_numbers_into_group(number, group)
		
		for counter in range(100):
			if not self.reduce_possibilites(groups):
				print "Solved or stopped after {0} steps".format(counter)
				break

	def place_possible_numbers_into_group(self, number, group):
		empty_cells = filter(lambda c: not c.has_value, group)

		if len(filter(lambda c: c.value == number, group)) == 0:
			map(lambda c: c.add_possible_value(number), empty_cells)
		else:
			map(lambda c: c.remove_possible_value(number), empty_cells)

	def reduce_possibilites(self, groups):
		if self.single_option(groups):
			return True

		if self.hidden_option(groups):
			return True

		if self.pointing_pair(groups):
			return True

		return False

	def single_option(self, groups):
		# single option strategy
		for group in groups:
			for cell in group:
				number = cell.set_value_from_single_possiblity()
				if number is not None:
					print "Naked single in cell {0},{1} set to value {2}".format(cell.x, cell.y, number)
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_block(cell.block)))
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_row(cell.x)))
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_column(cell.y)))
					return True
		return False

	def hidden_option(self, groups):
		# hidden option strategy
		for number in range(1, 10):
			for group in groups:
				hidden_possibility = filter(lambda c: c.contains_possibility(number), group)
				if len(hidden_possibility) == 1:
					cell = hidden_possibility[0]
					cell.set_value(number)
					print "Hidden single in cell {0},{1} set to value {2}".format(cell.x, cell.y, number)
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_block(cell.block)))
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_row(cell.x)))
					map(lambda c: c.remove_possible_value(number), self.group_cells(lambda c: c.in_column(cell.y)))
					return True

		return False

	def pointing_pair(self, groups):
		# pointing pair strategy
		for block in range(9):
			
			group = self.group_cells(lambda c: c.in_block(block))

			for cell in group:
				candidates = filter(lambda c:
					(c != cell)
					and (c.same_row_as(cell) or c.same_column_as(cell))
					and len(c.possible_values.intersection(cell.possible_values)) > 0,
					group)

				if len(candidates) == 1:
					candidate_cell = candidates[0]
					print "Pointing pair found in cells {0},{1} and {2},{3}".format(
						cell.x, cell.y, candidate_cell.x, candidate_cell.y)

					other_cells = []
					if cell.x == candidate_cell.x:
						other_cells = self.group_cells(lambda c: c.in_row(cell.x) and c.block != cell.block and not c.has_value)
					if cell.y == candidate_cell.y:
						other_cells = self.group_cells(lambda c: c.in_column(cell.y) and c.block != cell.block and not c.has_value)

					if len(other_cells) > 0:
						value_removed = False
						for possible_value in cell.possible_values.intersection(candidate_cell.possible_values):
							for cell in other_cells:
								if cell.contains_possibility(possible_value):
									cell.remove_possible_value(possible_value)
									value_removed = True

						if value_removed:
							return True
						else:
							break
					

		return False

	def group_cells(self, predicate):
		cells = []
		for row in self.grid:
			for cell in row:
				if predicate(cell):
					cells.append(cell)

		return cells

	def print_grid(self):
		def print_row(row): print " ".join([str(cell) for cell in row])

		for row in self.grid:
			print_row(row)

game = Game("grid")
game.solve_grid()
print ""
game.print_grid()