import numpy as np
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
      if(board[i][j] > 0 ):
        print(board[i][j], end="  |  ")
      else:
        print(" ", end="  |  ")
    print()
    bot_filler()

board = np.zeros((9,9), dtype=int)
easy = np.array([
  [0,9,0,0,0,5,2,3,0],
  [7,0,1,0,0,2,6,0,9],
  [5,0,0,0,7,9,0,0,4],
  [2,0,6,0,0,0,7,1,0],
  [0,1,0,0,0,0,0,2,0],
  [0,7,3,0,0,0,4,0,6],
  [9,0,0,5,1,0,0,0,8],
  [1,0,7,3,0,0,5,0,2],
  [0,8,5,4,0,0,0,6,0]
])

display_board(easy)