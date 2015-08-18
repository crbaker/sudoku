from grid import block_predicates, block_for_cell

class Cell:	

	def __init__(self, x, y, value):
		self.value = value
		self.has_value = value > 0

		self.x = x
		self.y = y		

		self.possible_values = set()
		self.impossible_values = set()

		self.block = self.calculate_block()

	def calculate_block(self):
		return block_for_cell(self)

	def current_value(self):
		return self.value

	def set_value(self, new_value):
		self.value = new_value
		self.possible_values.clear()
		self.has_value = new_value != 0

	def current_possibilities(self):
		if len(self.possible_values) > 0:
			return "".join([str(possible) for possible in self.possible_values])
		else:
			return ""

	def add_possible_value(self, possible_value):
		if not possible_value in self.impossible_values:
			self.possible_values.add(possible_value)

	def remove_possible_value(self, possible_value):
		self.possible_values.discard(possible_value)
		self.impossible_values.add(possible_value)

	def contains_possibility(self, possibility):
		return not self.has_value and possibility in self.possible_values

	def number_of_possibilities(self):
		return len(self.possible_values)

	def set_value_from_single_possiblity(self):
		if len(self.possible_values) == 1:
			self.value = self.possible_values.pop();
			return self.value

	def same_row_as(self, other):
		return self.x == other.x

	def same_column_as(self, other):
		return self.y == other.y

	def in_block(self, block):
		return block_predicates()[block](self.x, self.y)

	def in_row(self, row):
		return self.x == row

	def in_column(self, column):
		return self.y == column

	def __str__(self):
		return str(self.value) + " (" + self.current_possibilities() + ")"

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self.x != other.x or self.y != other.y