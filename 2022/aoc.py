def _get_input_data():
  import os.path
  import subprocess
  import sys

  year = int(__file__.split('/')[-2])
  day = int(sys.argv[0][2:4])

  assert 1 <= day <= 25, f"Invalid day: {day}"
  assert 2015 <= year, f"Invalid year: {year}"

  input_file = sys.argv[1] if len(sys.argv) > 1 else f'{day:02}.in'

  print_input = False
  if not os.path.exists(input_file) and os.path.exists('../.session'):
    with open('../.session') as file:
      session=file.read().strip()
    cmd = ['curl', f'https://adventofcode.com/{year}/day/{day}/input', '--cookie', f'session={session}']
    process = subprocess.Popen(cmd, shell=False, stdout=open(input_file, 'w'))
    process.wait()
    print()
    print_input = True

  data = open(input_file).read().rstrip()
  lines = data.split('\n')
  number_of_lines = len(lines)
  empty = [i for i,line in enumerate(lines) if not line]

  if print_input:
    print(data)
    print()

  print(f'Advent of Code {year}/{day:02} [https://adventofcode.com/{year}/day/{day}]')
  print(f'Input file \'{input_file}\' contains {number_of_lines} lines and {len(empty)} empty lines.\n')
  return data, lines, number_of_lines, empty

DATA, LINES, N, EMPTY = _get_input_data()

def parseLines(f):
  return [f(line.rstrip()) for line in LINES]

def replaceLines(A, B=''):
  global LINES
  LINES = [line.replace(A, B) for line in LINES]
