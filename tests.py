import unittest
from cell import Cell

class TestStringMethods(unittest.TestCase):

  def test_cell_created_with_zero_value_has_no_value(self):
    cell = Cell(0, 0, 0)

    self.assertFalse(cell.has_value)

  def test_cell_created_with_no_value(self):
    cell = Cell(0, 0, None)

    self.assertEqual(cell.value, None)
    self.assertFalse(cell.has_value)

  def test_cell_created_with_value(self):
    cell = Cell(0,0,1)

    self.assertEqual(cell.value, 1)
    self.assertTrue(cell.has_value)

  def test_add_possible_value(self):
    cell = Cell(0,0,1)
    self.assertEqual(0, len(cell.possible_values))
    cell.add_possible_value(1)
    cell.add_possible_value(2)
    self.assertEqual(2, len(cell.possible_values))

  def test_cannot_add_duplicate_possible_value(self):
    cell = Cell(0,0,1)
    self.assertEqual(0, len(cell.possible_values))
    cell.add_possible_value(1)
    cell.add_possible_value(1)
    self.assertEqual(1, len(cell.possible_values))

  def test_add_possible_value(self):
    cell = Cell(0, 0, 1)
    self.assertEqual(0, len(cell.possible_values))
    cell.add_possible_value(1)
    cell.add_possible_value(2)
    self.assertEqual(2, len(cell.possible_values))

  def test_cell_in_quadrant_0(self):
    cell = Cell(1, 2, 1)
    self.assertTrue(cell.in_quadrant(0))

  def test_cell_is_not_in_quadrant_0(self):
    cell = Cell(1, 3, 1)
    self.assertFalse(cell.in_quadrant(0))    

if __name__ == '__main__':
    unittest.main()