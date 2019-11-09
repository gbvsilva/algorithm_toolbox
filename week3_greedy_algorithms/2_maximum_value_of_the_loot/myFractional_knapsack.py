# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	# write your code here
	lst = list()
	for v_w in zip(values, weights):
		lst.append((v_w[0]/v_w[1], v_w[0], v_w[1]))
	lst = sorted(lst)
	for i in reversed(range(len(lst))):
		if lst[i][2] <= capacity:
			value += lst[i][1]
			capacity -= lst[i][2]
		else:
			value += lst[i][1]/lst[i][2]*capacity
			break
	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.4f}".format(opt_value))
