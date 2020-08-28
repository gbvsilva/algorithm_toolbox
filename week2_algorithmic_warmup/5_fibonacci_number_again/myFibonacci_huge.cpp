#include <iostream>
#define max 100000000000000

long long fn_mod_m(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
	long long remainder;

    for (long long i = 2; i <= n; ++i) {
        remainder = (previous+current) % m;
		previous = current;
		current = remainder;
    }

    return remainder;
}

long long get_pisano_length(long long m) {
	if (m <= 1)
    	return m;
	long long previous, current, pisanoLen, remainder;
	previous = 0;
	current = 1;
	pisanoLen = 0;
	//std::cout << "0 1 ";
	for(long long i=2; i <= max; ++i) {
		remainder = (previous+current)%m;
		previous = current;
		current = remainder;
		pisanoLen++;
		if(current == 1 && previous == 0)
			break;
	}
	//std::cout << "Pisano Len: "<< pisanoLen << '\n';
	return pisanoLen;
}

int main() {
    long long n, m, ans;
    std::cin >> n >> m;
	if(n % m < n) {
		ans = n % get_pisano_length(m);
		std::cout << fn_mod_m(ans, m) << '\n';
	}
	else {
		ans = fn_mod_m(n, m);
		std::cout << ans << '\n';
	}

	return 0;
}
