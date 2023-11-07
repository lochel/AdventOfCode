#!../.env/bin/python3

LINES = [line.strip() for line in open('07.in')]
N = len(LINES)
print(f'input contains {N} lines')


# 1.
# --------------------------------------
def problem1():
  line = LINES[0]
  pos = [int(x) for x in line.split(',')]
  s = []
  for x in range(min(pos), max(pos)+1):
    s.append(sum([abs(a-x) for a in pos]))
  return min(s)


# 2.
# --------------------------------------
def problem2():
  def cost(x):
    return (x*x+x)//2
  line = LINES[0]
  pos = [int(x) for x in line.split(',')]
  s = []
  for x in range(min(pos), max(pos)+1):
    s.append(sum([cost(abs(a-x)) for a in pos]))
  return min(s)


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
