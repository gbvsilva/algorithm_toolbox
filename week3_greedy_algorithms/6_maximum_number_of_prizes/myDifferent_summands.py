# Uses python3
import sys

def optimal_summands(n):
	summands = []
	#write your code here
	if n <= 2:
		return [n]
	rest = 0
	i = 1
	while i*2 < n:
		summands.append(i)
		n -= i
		i += 1
	summands.append(n)
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
