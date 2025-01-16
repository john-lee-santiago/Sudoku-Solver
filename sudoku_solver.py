import numpy as np
import cell
def display_board(board):
  def new_line():
    for i in range(9*5 + 10):
      print("_", end="")
    print()

  def top_filler():
    for i in range(9):
      print("|     ", end="")
    print("|")

  def bot_filler():
    for i in range(9):
      print("|_____", end="")
    print("|")

  new_line()
  for i in range(len(board)):
    top_filler()
    print("|", end="  ")
    for j in range(len(board[i])):
      if(board[i][j].value > 0 ):
        print(board[i][j].value, end="  |  ")
      else:
        print(" ", end="  |  ")
    print()
    bot_filler()

def update_board(board, row, column, first_cell):
  fc_row = first_cell[0]
  fc_column = first_cell[1]
  blocks[board[row, column].block].remove(board[row, column].value)
  for i in range(fc_row, fc_row + 3):
    for j in range(fc_column, fc_column + 3):
      if board[i, j].value == 0:
        board[i, j].possible_values = blocks[board[i, j].block]
  
  rows[row].remove(sudoku_board[row, column].value)
  for j in range(9):
    if board[row, j].value == 0:
      board[row, j].possible_values = rows[row]

  columns[column].remove(sudoku_board[row, column].value)
  for i in range(9):
    if board[i, column].value == 0:
      board[i, column].possible_values = columns[column]

# https://www.websudoku.com/?level=1&set_id=2574551442
def fill_easy_board(board):
  sudoku_board[0,1].value = 9
  sudoku_board[0,5].value = 5
  sudoku_board[0,6].value = 2
  sudoku_board[0,7].value = 3
  sudoku_board[1,0].value = 7
  sudoku_board[1,2].value = 1
  sudoku_board[1,5].value = 2
  sudoku_board[1,6].value = 6
  sudoku_board[1,8].value = 9
  sudoku_board[2,0].value = 5
  sudoku_board[2,4].value = 7
  sudoku_board[2,5].value = 9
  sudoku_board[2,8].value = 4
  sudoku_board[3,0].value = 2
  sudoku_board[3,2].value = 6
  sudoku_board[3,6].value = 7
  sudoku_board[3,7].value = 1
  sudoku_board[4,1].value = 1
  sudoku_board[4,7].value = 2
  sudoku_board[5,1].value = 7
  sudoku_board[5,2].value = 3
  sudoku_board[5,6].value = 4
  sudoku_board[5,8].value = 6
  sudoku_board[6,0].value = 9
  sudoku_board[6,3].value = 5
  sudoku_board[6,4].value = 1
  sudoku_board[6,8].value = 8
  sudoku_board[7,0].value = 1
  sudoku_board[7,2].value = 7
  sudoku_board[7,3].value = 3
  sudoku_board[7,6].value = 5
  sudoku_board[7,8].value = 2
  sudoku_board[8,1].value = 8
  sudoku_board[8,2].value = 5
  sudoku_board[8,3].value = 4
  sudoku_board[8,7].value = 6
# https://www.websudoku.com/?level=4&set_id=5417957080
def fill_evil_board(board):
  sudoku_board[0,0].value = 5
  sudoku_board[0,4].value = 1
  sudoku_board[0,8].value = 3
  sudoku_board[1,0].value = 8
  sudoku_board[1,3].value = 9
  sudoku_board[1,4].value = 5
  sudoku_board[1,6].value = 6
  sudoku_board[2,1].value = 7
  sudoku_board[2,6].value = 4
  sudoku_board[2,7].value = 9
  sudoku_board[3,5].value = 1
  sudoku_board[4,1].value = 3
  sudoku_board[4,3].value = 8
  sudoku_board[4,5].value = 7
  sudoku_board[4,7].value = 5
  sudoku_board[5,3].value = 5
  sudoku_board[6,1].value = 6
  sudoku_board[6,2].value = 5
  sudoku_board[6,7].value = 3
  sudoku_board[7,2].value = 4
  sudoku_board[7,4].value = 2
  sudoku_board[7,5].value = 9
  sudoku_board[7,8].value = 6
  sudoku_board[8,0].value = 7
  sudoku_board[8,4].value = 6
  sudoku_board[8,8].value = 9

sudoku_board = np.empty((9,9), dtype=object)
# Keeps track of values that have already been used
rows = {row: set(range(1,10)) for row in range(9)}
columns = {column: set(range(1,10)) for column in range(9)}
blocks = {block: set(range(1,10)) for block in range(9)}
# Used to reference which cells belong to a 3x3 block
block_first_cell = {
  0 : (0,0),
  1 : (0,3),
  2 : (0,6),
  3 : (3,0),
  4 : (3,3),
  5 : (3,6),
  6 : (6,0),
  7 : (6,3),
  8 : (6,6),
}
cells_remaining = 81

for i in range(9):
  for j in range(9):
    sudoku_board[i,j] = cell.Cell(0,i,j)

# TODO: import initial board state
fill_easy_board(sudoku_board)
#fill_evil_board(sudoku_board)

# Reads and updates intial sudoku board state
for i in range(9):
  for j in range(9):
    if sudoku_board[i,j].value > 0:
      cells_remaining -= 1
      update_board(sudoku_board, i, j, block_first_cell[sudoku_board[i,j].block])

#visual aid
#for i in range(9):
#  for j in range(9):
#    if board1[i,j].value == 0:
#      print(f"{i}:{j}", end=" ")
#      print(board1[i][j].possible_values, end=", ")
#      print(len(board1[i][j].possible_values))

#loop_counter = 0
# Solving algorithm
# TODO: implement algorithm when no cells contain a single possible value
while cells_remaining > 0:
#  loop_counter += 1
  for i in range(9):
    for j in range(9):
      if sudoku_board[i, j].value == 0 and len(sudoku_board[i][j].possible_values) == 1:
        sudoku_board[i, j].value = sudoku_board[i][j].possible_values.pop()
        cells_remaining -= 1
        update_board(sudoku_board, i, j, block_first_cell[sudoku_board[i,j].block])
#  print(loop_counter)

display_board(sudoku_board)
#print(f"Number of loops: {loop_counter}")