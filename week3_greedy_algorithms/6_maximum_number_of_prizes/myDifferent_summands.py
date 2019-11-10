# Uses python3
import sys

def optimal_summands(n):
	summands = []
	#write your code here
	if n <= 2:
		return [[n]]
	memo = []
	max_len = 0
	while True:
		lst = [1]
		i = 2
		aux_n = n-1
		while aux_n > i:
			if aux_n - i > i and i not in memo:
				aux_n -= i
				lst.append(i)
				memo.append(i)

			i += 1
		if i in memo:
			break
		elif sum(lst)+i == n:
			memo.append(i)
			lst.append(i)
			if len(lst) >= max_len:
				max_len = len(lst)
				summands.append(lst)
		
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	
	if len(summands) <= 0:
		print(1)
		print(n, end=' ')
	else:
		print(len(summands[0]))
		for lst in summands:
			for x in lst:
				print(x, end=' ')
			print()

