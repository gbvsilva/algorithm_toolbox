#include <iostream>

long long gcd_naive(long long a, long long b) {
  long long current_gcd = 1;
  for (long long d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

long long gcd_fast(long long a, long long b) {
	long long aux;
	if(a < b) {
		aux = a;
		a = b;
		b = aux;
	}

	while(a % b != 0) {
		aux = b;
		b = a%b;
		a = aux;
	}

	return b;
}

int main() {
  int a, b;
  //std::cin >> a >> b;
  //std::cout << gcd_naive(a, b) << std::endl;
  //std::cout << gcd_fast(a, b) << std::endl;
  while(true) {
	a = rand() % 1000000000 + 2;
	b = rand() % 1000000000 + 2;
	std::cout << a << ' ' << b << "\n";
	long long res1 = gcd_naive(a, b);
	long long res2 = gcd_fast(a, b);
	if(res1 != res2) {
		std::cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
		break;
	}else
		std::cout << "OK\n";
  }  
  return 0;
}
