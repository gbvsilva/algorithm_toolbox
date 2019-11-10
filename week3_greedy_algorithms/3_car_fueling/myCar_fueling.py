# python3
import sys


def compute_min_refills(distance, tank, stops):
	# write your code here
	min_refills = 0
	last_stop = 0
	stops.append(distance)
	for i in range(len(stops)-1):
		if stops[i] + tank < stops[i+1]:
			return -1
		if tank + last_stop < stops[i+1]:
			min_refills += 1
			last_stop = stops[i]

	return min_refills


if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
