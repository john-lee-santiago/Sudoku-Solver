class Cell:
  def __init__(self, value, row, column):
    self._value = value
    self._row = row
    self._column = column
    self._block = self.init_block(row, column)
    self._possible_values = set(range(1,10))

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    self._value = value
    self._possible_values = set()
  
  @property
  def row(self):
    return self._row
  
  @property
  def column(self):
    return self._column

  @property
  def block(self):
    return self._block
  
  @property
  def possible_values(self):
    return self._possible_values
  
  @possible_values.setter
  def possible_values(self, values):
    self._possible_values &= values

  def init_block(self, row, column):
    block_case = {
      (range(0,3), range(0,3)): 0,
      (range(0,3), range(3,6)): 1,
      (range(0,3), range(6,9)): 2,
      (range(3,6), range(0,3)): 3,
      (range(3,6), range(3,6)): 4,
      (range(3,6), range(6,9)): 5,
      (range(6,9), range(0,3)): 6,
      (range(6,9), range(3,6)): 7,
      (range(6,9), range(6,9)): 8
    }
    for (range1, range2), block in block_case.items():
      if row in range1 and column in range2:
        return block