# Uses python3
import sys
#import time

def optimal_summands(n):
	summands = []
	#write your code here
	if n <= 2:
		return [n]
	rest = 0
	for i in range(1, n):
		if sum(summands)+i > n:
			rest = n - sum(summands)
			break
		summands.append(i)

	summands[-1] += rest
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	start = time.time()
	elapsed = 0
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
	#elapsed = time.time() - start
	#print("Time -> "+str(elapsed))
