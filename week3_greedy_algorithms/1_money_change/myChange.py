# python3
import sys

def get_change(m):
	count = 0
	while m - 10 >= 0:
		count += 1
		m -= 10
	while m - 5 >= 0:
		count += 1
		m -= 5
	while m - 1 >= 0:
		count += 1
		m -= 1
	return count

if __name__ == '__main__':
	m = int(input())
	print(get_change(m))
