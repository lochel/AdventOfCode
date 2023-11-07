#!../.env/bin/python3

lines = [line.strip() for line in open('04.in')]
N = len(lines)


def won(board):
  for i in range(5):
    if board[i*5+0] + board[i*5+1] + board[i*5+2] + board[i*5+3] + board[i*5+4] == "xxxxx":
      return True
  for i in range(5):
    if board[0*5+i] + board[1*5+i] + board[2*5+i] + board[3*5+i] + board[4*5+i] == "xxxxx":
      return True
  return False


def newNumber2(a, b):
  if a != b:
    return a
  return 'x'
def newNumber(board, number):
  return [newNumber2(n, number) for n in board]


# 1.
# --------------------------------------
def problem1():
  boards = []
  for i in range(2, N, 6):
    board = lines[i].split(' ') + lines[i+1].split(' ') + lines[i+2].split(' ') + lines[i+3].split(' ') + lines[i+4].split(' ')
    board = list(filter(None, board))
    assert len(board) == 25, board
    boards.append(board)

  numbers = lines[0].split(',')
  for number in numbers:
    boards = [newNumber(board, number) for board in boards]
    for board in boards:
      if won(board):
        board = [int(n) for n in board if n != 'x']
        answer1 = int(number) * sum(board)
        return answer1


# 2.
# --------------------------------------
def problem2():
  boards = []
  for i in range(2, N, 6):
    board = lines[i].split(' ') + lines[i+1].split(' ') + lines[i+2].split(' ') + lines[i+3].split(' ') + lines[i+4].split(' ')
    board = list(filter(None, board))
    assert len(board) == 25, board
    boards.append(board)

  won__=len(boards)*[False]
  numbers = lines[0].split(',')
  for number in numbers:
    boards = [newNumber(board, number) for board in boards]
    for id,board in enumerate(boards):
      if won(board) and not won__[id]:
        won__[id] = True
        board = [int(n) for n in board if n != 'x']
        answer2 = int(number) * sum(board)
  return answer2


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
