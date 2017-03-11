#include <iostream>
#include <utility>
#include <cassert>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}


int gcd_fast(int &a, int &b){
  if (b > a){
    int tmp = a;
    a = b;
    b= tmp;
  }

  if (b == 0){
    return a;
  }else if(b == 1){
    return 1;
  } else{

    int r = a % b;
    gcd_fast(b, r);
  }
}

void gcd_fast_test(){

  int a = 35;
  int b = 18;

  int case1= gcd_fast(a, b);
  std::cout << "case1: " << case1 << std::endl;
  assert(case1 == 1);

  a = 12;
  b = 8;
  int case2= gcd_fast(a, b);
  std::cout << "case2: " << case2 << std::endl;
  assert(case2 == 4);

  a = 20;
  b = 25;

  int case3= gcd_fast(a, b);
  std::cout << "case3: " << case3 << std::endl;
  assert(case3 == 5);

  a = 28851538;
  b = 1183019;
  int case4= gcd_fast(a, b);
  std::cout << "case4: " << case4 << std::endl;
  assert(case4 == 17657);

  a = 6;
  b = 12;
  int case5= gcd_fast(a, b);
  std::cout << "case5: " << case5 << std::endl;
  assert(case5 == 6);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd_fast(a, b) << std::endl;

  //  gcd_fast_test();

  return 0;
}
