#include <iostream>
#include <cassert>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
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

long long lcm_fast(int a, int b){
  int gcd = gcd_fast(a, b);
  long long tmp = (long long) a * b;
  long long lcm = tmp / gcd;
  return lcm;
}

void test_lcm(){
  int a = 6;
  int b = 8;

  long long case1 = lcm_fast(a, b);
  std::cout << "case1: " << case1 << std::endl;
  assert(case1 == 24);

  a = 28851538;
  b = 1183019;

  long long case2 = lcm_fast(a, b);
  std::cout << "case2: " << case2 << std::endl;
  assert(case2 == 1933053046);

  a = 14159572;
  b = 63967072;

  long long case3 = lcm_fast(a, b);
  std::cout << "case3: " << case3 << std::endl;
  assert(case3 == 226436590403296);

  a = 1827116622;
  b = 251772294;

  long long case4 = lcm_fast(a, b);
  std::cout << "case4: " << case4 << std::endl;
  assert(case4 == 76669557221078478);
}


int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_fast(a, b) << std::endl;
    
  // test_lcm();
  return 0;
}
