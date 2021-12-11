from pathlib import Path
import sys

example = """199
200
208
210
200
207
240
269
260
263"""

handle = Path('input/day01-puzzle1.txt')
depths = handle.read_text()

def count_increases(depths):
	depths = [int(d) for d in depths.splitlines()]
	increases = 0
	for i, depth in enumerate(depths):
		if not i == 0:
			if depth > depths[i - 1]:
				increases += 1
	return increases

assert count_increases(example) == 7, 'example failed'
print(f'depth increased {count_increases(depths)}')

def count_increases_threes(depths):
	depths = [int(d) for d in depths.splitlines()]
	windows = [depths[i:i+3] for i, _ in enumerate(depths)]
	increases = 0
	for i, w in enumerate(windows):
		if not i == 0 and not len(w) < 3:
			if sum(w) > sum(windows[i - 1]):
				increases += 1
	return increases

assert count_increases_threes(example) == 5, 'example failed'
print(f'depth increased {count_increases_threes(depths)}')
