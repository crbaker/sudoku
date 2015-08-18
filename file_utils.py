from cell import Cell

class FileReader:

	grid_size = 9
	
	def __init__(self, file_name):
		self.file_content = self.read_file(file_name)

		if not self.validate_content(self.file_content):
			raise ValueError("The file does not have the correct format")

	def validate_content(self, file_content):
		return len(file_content) is FileReader.grid_size * FileReader.grid_size

	def read_file(self, file_name):
		f = open(file_name, "r")
		file_content = f.read()
		f.close()
		return file_content

	def build_grid(self):
		grid = [[0 for x in range(FileReader.grid_size)] for x in range(FileReader.grid_size)]
		index = 0
		for i in range(len(grid)):
			row = grid[x]
			for j in range(len(row)):
				grid[i][j] = Cell(i, j, int(self.file_content[index]))
				index += 1

		return grid