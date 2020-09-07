#include <iostream>

int get_change(int m) {
	//write your code here
	int counter = 0;
	while(m - 10 >= 0) {
		counter++;
		m -= 10;
	}

	while(m - 5 >= 0) {
		counter++;
		m -= 5;
	}

	while(m - 1 >= 0) {
		counter++;
		m -= 1;
	}
  return counter;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
