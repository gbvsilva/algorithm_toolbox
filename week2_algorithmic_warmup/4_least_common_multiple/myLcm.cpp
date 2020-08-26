#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long lcm_fast(long long a, long long b) {
	long long c, d, aux;
	if(a < b) {
		aux = a;
		a = b;
		b = aux;
	}
	c = a;
	d = b;
	while(a % b != 0) {
		aux = b;
		b = a%b;
		a = aux;
	}
	return (c/b)*d;
}

void stress_test() {
	long long a, b, res1, res2;
	while(true) {
		a = rand() % 10000000 + 2;
		b = rand() % 10000000 + 2;
		std::cout << a << ' ' << b << "\n";
		res1 = lcm_naive(a, b);
		res2 = lcm_fast(a, b);

		if(res1 != res2) {
			std::cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
			break;
		}else
			std::cout << "OK\n";
	}
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;
  //stress_test();
  return 0;
}
