#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  data = aoc.DATA

  stack = []
  i = 0
  while i < len(data):
    if data[i:i+4] == 'mul(':
      stack.append('mul(')
      i += 4
    elif data[i] == ',':
      stack.append(',')
      i += 1
    elif data[i] == ')':
      stack.append(')')
      i += 1
    elif data[i:i+3].isnumeric():
      stack.append(int(data[i:i+3]))
      i += 3
    elif data[i:i+2].isnumeric():
      stack.append(int(data[i:i+2]))
      i += 2
    elif data[i:i+1].isnumeric():
      stack.append(int(data[i:i+1]))
      i += 1
    else:
      stack.append(None)
      i += 1

  answer = 0
  i = 0
  while i < len(stack) - 4:
    if stack[i] == 'mul(' and isinstance(stack[i+1], int) and stack[i+2] == ',' and isinstance(stack[i+3], int) and stack[i+4] == ')':
      answer += stack[i+1] * stack[i+3]
      i += 4
    else:
      i += 1
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  data = aoc.DATA

  stack = []
  i = 0
  while i < len(data):
    if data[i:i+7] == "don't()":
      stack.append(False)
      i += 7
    elif data[i:i+4] == 'do()':
      stack.append(True)
      i += 4
    elif data[i:i+4] == 'mul(':
      stack.append('mul(')
      i += 4
    elif data[i] == ',':
      stack.append(',')
      i += 1
    elif data[i] == ')':
      stack.append(')')
      i += 1
    elif data[i:i+3].isnumeric():
      stack.append(int(data[i:i+3]))
      i += 3
    elif data[i:i+2].isnumeric():
      stack.append(int(data[i:i+2]))
      i += 2
    elif data[i:i+1].isnumeric():
      stack.append(int(data[i:i+1]))
      i += 1
    else:
      stack.append(None)
      i += 1

  answer = 0
  i = 0
  do = True
  while i < len(stack) - 4:
    if isinstance(stack[i], bool):
      do = stack[i]
      i += 1
    elif do and stack[i] == 'mul(' and isinstance(stack[i+1], int) and stack[i+2] == ',' and isinstance(stack[i+3], int) and stack[i+4] == ')':
      answer += stack[i+1] * stack[i+3]
      i += 4
    else:
      i += 1
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
