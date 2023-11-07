#!../.env/bin/python3

from collections import defaultdict

LINES = [line.strip() for line in open('06.in')]
N = len(LINES)
print(f'input contains {N} lines')

# 1.
# --------------------------------------
def problem1():
  for line in LINES:
    fish = [int(x) for x in line.split(',')]
    for i in range(80):
      fish = [x-1 for x in fish]
      new = [8 for x in fish if x < 0]
      fish = fish + new
      fish = [6 if x<0 else x for x in fish]
    return len(fish)


# 2.
# --------------------------------------
def problem2():
  fish = [int(x) for x in LINES[0].split(',')]

  X = defaultdict(int)
  for f in fish:
    X[f] += 1

  for _ in range(256):
    Y = defaultdict(int)
    for f, cnt in X.items():
      if f == 0:
        Y[6] += cnt
        Y[8] += cnt
      else:
        Y[f-1] += cnt

      X = Y
  return sum(X.values())


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
