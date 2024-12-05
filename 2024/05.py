#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  rules = aoc.parseLines(aoc.CHUNKS[0], lambda line : line.split('|'))
  rules = [[int(x) for x in line] for line in rules]

  pages = aoc.parseLines(aoc.CHUNKS[1], lambda line : line.split(','))
  pages = [[int(x) for x in line] for line in pages]

  answer = 0
  for page in pages:
    ok = True
    for [a, b] in rules:
      if a in page and b in page:
        if page.index(a) > page.index(b):
          ok = False
    if ok:
      answer += page[len(page)//2]

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  rules = aoc.parseLines(aoc.CHUNKS[0], lambda line : line.split('|'))
  rules = [[int(x) for x in line] for line in rules]

  pages = aoc.parseLines(aoc.CHUNKS[1], lambda line : line.split(','))
  pages = [[int(x) for x in line] for line in pages]

  def page_ok(page, r):
    for [a, b] in r:
      if a in page and b in page:
        if page.index(a) > page.index(b):
          return False
    return True

  answer = 0
  for page in pages:
    if page_ok(page, rules):
      continue

    while not page_ok(page, rules):
      for [a, b] in rules:
        if a in page and b in page:
          if page.index(a) > page.index(b):
            page[page.index(a)], page[page.index(b)] = page[page.index(b)], page[page.index(a)]
    answer += page[len(page)//2]
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
