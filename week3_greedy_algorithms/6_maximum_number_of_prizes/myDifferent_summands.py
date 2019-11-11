# Uses python3
import sys

def optimal_summands(n):
	summands = []
	#write your code here
	if n <= 2:
		return [[n]]
	numbers = []
	sum_cache = 0
	for i in range(1, n):
		if sum(numbers)+i > n:
			sum_cache = n - sum(numbers)
			break
		numbers.append(i)

	print(len(numbers))
	if sum_cache > 0:
		numbers[-1] += sum_cache
		summands.append(numbers.copy())
		numbers[-1] -= sum_cache
		for i in range(1, sum_cache):
			temp = numbers[-1-i]
			del numbers[-1-i]
			numbers.append(temp+sum_cache)
			print(*numbers)
			del numbers[-1]
			numbers.insert(-i, temp)
	else:
		for num in numbers:
			print(x, end=' ')

		
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	
	"""if len(summands) <= 0:
		print(1)
		print(n, end=' ')
	else:
		print(len(summands[0]))
		for lst in summands:
			for x in lst:
				print(x, end=' ')
			print()"""
