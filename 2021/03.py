#!../.env/bin/python3

import sys

answer1, answer2 = None, None
input_file = sys.argv[1] if len(sys.argv) > 1 else '03.in'
lines = [line.strip() for line in open(input_file)]

# 1.
# --------------------------------------
answer1=list('000000000000')
for line in lines:
  answer1 = [int(f)+int(b) for (f, b) in zip(answer1, list(line))]

a, b = 0, 0
for x, i in zip(answer1, range(11, -1, -1)):
  if x > 500:
    a += 1<<i
  else:
    b += 1<<i
answer1 = a*b
print(f'Answer 1: {answer1}')

# 2.
# --------------------------------------
lines2 = lines
for r in range(12):
  threshold = len(lines)/2
  answer1=list('000000000000')
  for line in lines:
    answer1 = [int(f)+int(b) for (f, b) in zip(answer1, list(line))]
  c = '1' if answer1[r] >= threshold else '0'
  lines = [line for line in lines if line[r] == c]
  #print(lines)
  if len(lines) == 1:
    oxygen_generator_rating = lines[0]
    oxygen_generator_rating = int(oxygen_generator_rating, 2)
    print(f'{oxygen_generator_rating=}')
    break

lines = lines2
for r in range(12):
  threshold = len(lines)/2
  answer1=list('000000000000')
  for line in lines:
    answer1 = [int(f)+int(b) for (f, b) in zip(answer1, list(line))]
  c = '0' if answer1[r] >= threshold else '1'
  lines = [line for line in lines if line[r] == c]
  #print(lines)
  if len(lines) == 1:
    CO2_scrubber_rating = lines[0]
    CO2_scrubber_rating = int(CO2_scrubber_rating, 2)
    print(f'{CO2_scrubber_rating=}')
    break

print(f'Answer 2: {oxygen_generator_rating*CO2_scrubber_rating}')
