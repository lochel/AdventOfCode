#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, 'Game ', '')
  lines = aoc.replaceLines(lines, ':', '')
  lines = aoc.replaceLines(lines, ',', '')
  lines = aoc.replaceLines(lines, ';', ' ; ;')
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  answer = 0
  for line in lines:
    #12 red cubes, 13 green cubes, and 14 blue cubes
    id = int(line[0])
    good = True

    for i in range(1, len(line), 2):
      if line[i] == ";":
        continue
      n = int(line[i])
      color = line[i+1]
      if color == "red" and n <= 12:
        pass
      elif color == "green" and n <= 13:
        pass
      elif color == "blue" and n <= 14:
        pass
      else:
        good = False
    if good:
      answer += id

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, 'Game ', '')
  lines = aoc.replaceLines(lines, ':', '')
  lines = aoc.replaceLines(lines, ',', '')
  lines = aoc.replaceLines(lines, ';', ' ; ;')
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  answer = 0
  for line in lines:
    #12 red cubes, 13 green cubes, and 14 blue cubes
    id = int(line[0])
    red = 0
    green = 0
    blue = 0

    for i in range(1, len(line), 2):
      if line[i] == ";":
        continue
      n = int(line[i])
      color = line[i+1]

      if color == "red":
        red = max(red, n)
      elif color == "green":
        green = max(green, n)
      elif color == "blue":
        blue = max(blue, n)
      else:
        print("Error")
    answer += red*blue*green

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
