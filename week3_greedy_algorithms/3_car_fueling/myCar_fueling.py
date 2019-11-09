# python3
import sys


def compute_min_refills(distance, tank, stops):
	# write your code here
	
	min_refills = 0
	#current_distance = 0
	previous_stop = 0
	#current_tank = tank
	for stop in stops:
		if previous_stop+tank >= distance:
			return min_refills
		if tank <= stop:
			min_refills += 1
		previous_stop = stop
	
	return -1

if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
