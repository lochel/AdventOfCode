#!../.env/bin/python3

import os.path
import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip().split(' ') for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')

# --------------------------------------
def RockPaperScissors(player1, player2):
  return {('B', 'C'): 'X', ('C', 'A'): 'X', ('A', 'B'): 'X',
          ('B', 'B'): 'Y', ('C', 'C'): 'Y', ('A', 'A'): 'Y',
          ('B', 'A'): 'Z', ('C', 'B'): 'Z', ('A', 'C'): 'Z',}[(player1, player2)]

def CalcScore(X):
  return {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}[X]

def CalcMove(player2, res):
  if res == 'Y':
    return player2

  if res == 'Z':
    if player2 == 'A':
      return 'B'
    if player2 == 'B':
      return 'C'
    if player2 == 'C':
      return 'A'

  if res == 'X':
    if player2 == 'A':
      return 'C'
    if player2 == 'B':
      return 'A'
    if player2 == 'C':
      return 'B'

# --------------------------------------
answer1, answer2 = 0, 0
for [a, b] in LINES:
  # part 1
  # Input A/X: Rock
  # Input B/Y: Paper
  # Input C/Z: Scissors
  # --------------------------------------
  if b == 'X':
    me = 'A'
  if b == 'Y':
    me = 'B'
  if b == 'Z':
    me = 'C'
  answer1 += CalcScore(me)
  answer1 += CalcScore(RockPaperScissors(me, a))

  # part 2
  # A: Rock       X: You Lost
  # B: Paper      Y: Draw
  # C: Scissors   Z: You won
  # --------------------------------------
  answer2 += CalcScore(CalcMove(a, b))
  answer2 += CalcScore(b)

# --------------------------------------
# 1. What would your total answer12 be if everything goes exactly according to your strategy guide?
# 2. What would your total answer12 be if everything goes exactly according to your strategy guide?
print(f'Answer 1: {answer1}')
print(f'Answer 2: {answer2}')
