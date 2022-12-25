#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '05.in'
LINES = [line.strip() for line in open(input_file)]

def isNice(s: str):
  # It contains at least three vowels (aeiou only), like aei, xazegov,
  # or aeiouaeiouaeiou.
  vowels = 'aeiou'
  if sum([s.count(v) for v in vowels]) < 3:
    return False

  # It contains at least one letter that appears twice in a row, like
  # xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
  ok = False
  for idx,v in enumerate(s):
    if idx == 0: continue
    if s[idx-1] == v:
      ok = True
      break
  if not ok: return False

  # It does not contain the strings ab, cd, pq, or xy, even if they
  # are part of one of the other requirements.
  if s.count('ab') > 0: return False
  if s.count('cd') > 0: return False
  if s.count('pq') > 0: return False
  if s.count('xy') > 0: return False

  return True

def isNice2(s: str):
  # It contains a pair of any two letters that appears at least twice
  # in the string without overlapping, like xyxy (xy) or aabcdefgaa
  # (aa), but not like aaa (aa, but it overlaps).
  ok = False
  for idx,v in enumerate(s):
    if idx == 0: continue
    if s.count(s[idx-1]+v) > 1:
      ok = True
      break
  if not ok: return False

  # It contains at least one letter which repeats with exactly one
  # letter between them, like xyx, abcdefeghi (efe), or even aaa.
  ok = False
  for idx,v in enumerate(s):
    if idx == 0: continue
    if idx == 1: continue
    if s[idx-2] == v:
      ok = True
      break
  if not ok: return False

  return True

# 1. How many strings are nice?
# ----------------------------------------
def problem1():
  answer = 0
  for line in LINES:
    if isNice(line): answer += 1
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  for line in LINES:
    if isNice2(line): answer += 1
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
