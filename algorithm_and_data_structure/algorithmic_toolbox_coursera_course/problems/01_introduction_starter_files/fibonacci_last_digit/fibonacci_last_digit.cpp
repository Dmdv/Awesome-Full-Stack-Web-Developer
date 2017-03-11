#include <iostream>
#include <cassert>

int get_fibonacci_last_digit_naive(int n) {
  if (n <= 1)
    return n;

  int previous = 0;
  int current  = 1;

  for (int i = 0; i < n - 1; ++i) {
    int tmp_previous = previous;
    previous = current;
    current = tmp_previous + current;
  }

  return current % 10;
}

int get_fibonacci_last_digit_fast(int n) {
  if (n <= 1)
    return n;

  int previous = 0;
  int current  = 1;

  for (int i = 0; i < n - 1; ++i) {
    int tmp_previous = previous;
    previous = current;
    current = tmp_previous + current;
    current = current % 10;
  }

  return current;
}

void test_solution(int n){

  assert(get_fibonacci_last_digit_fast(0) == 0);
  assert(get_fibonacci_last_digit_fast(1) == 1);
  assert(get_fibonacci_last_digit_fast(331) == 9);
  assert(get_fibonacci_last_digit_fast(327305) == 5);
}

int main() {
  int n;
  std::cin >> n;
  int c = get_fibonacci_last_digit_fast(n);
  std::cout << c << '\n';

  // test_solution(100);
}
