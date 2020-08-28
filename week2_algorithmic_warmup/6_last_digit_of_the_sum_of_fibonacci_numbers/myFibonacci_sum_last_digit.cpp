#include <iostream>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int fibonacci_sum_fast(long long n) {
	if(n <= 1)
		return n;
	long long a=0, b=1, c, sum=1;
	for(int i=0; i < n-1; ++i) {
		c = a;
		a = b;
		b = (b % 10) + (c % 10);
		sum = (sum % 10) + (b % 10);
	}
	return sum % 10;
}

int main() {
    long long n = 0, res1, res2;
    std::cin >> n;
    //std::cout << fibonacci_sum_naive(n) << '\n';
	std::cout << fibonacci_sum_fast(n) << '\n';
	/*while(true) {
		n = rand() % 10000000000 + 2;
		std::cout << n << '\n';
		res1 = fibonacci_sum_naive(n);
		res2 = fibonacci_sum_fast(n);
		if(res1 != res2) {
			std::cout << "Wrong answer: " << res1 << ' ' << res2 << '\n';
			break;
		}else
			std::cout << "OK\n";
	}*/
}
