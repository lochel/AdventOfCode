#!../.env/bin/python3

answer1, answer2 = None, None
lines = [line.strip().split(' ') for line in open('02.in')]

# 1.
# ----------------------------------------
x, z, aim = 0, 0, 0
for [cmd, value] in lines:
  value = int(value)
  if cmd == 'forward':
    x += value
    z += aim*value
  elif cmd == 'down':
    z += value
  elif cmd == 'up':
    z -= value
  else:
    print(cmd, value)
    exit(0)
print(f'Answer 1: {x*z}')


# 2.
# ----------------------------------------
x, z, aim = 0, 0, 0
for [cmd, value] in lines:
  value = int(value)
  if cmd == 'forward':
    x += value
    z += aim*value
  elif cmd == 'down':
    aim += value
  elif cmd == 'up':
    aim -= value
  else:
    print(cmd, value)
    exit(0)
print(f'Answer 2: {x*z}')
