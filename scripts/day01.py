from pathlib import Path
from utils import get_input

def count_increases(depths):
	depths = [int(d) for d in depths.splitlines()]
	increases = 0
	for i, depth in enumerate(depths):
		if not i == 0:
			if depth > depths[i - 1]:
				increases += 1
	return increases

def count_increases_threes(depths):
	depths = [int(d) for d in depths.splitlines()]
	windows = [depths[i:i+3] for i, _ in enumerate(depths)]
	increases = 0
	for i, w in enumerate(windows):
		if not i == 0 and not len(w) < 3:
			if sum(w) > sum(windows[i - 1]):
				increases += 1
	return increases

if __name__ == '__main__':
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

	depths = get_input('day01.txt')

	assert count_increases(example) == 7, 'example failed'
	print(f'depth increased {count_increases(depths)}')

	assert count_increases_threes(example) == 5, 'example failed'
	print(f'depth increased {count_increases_threes(depths)}')