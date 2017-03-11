#include <iostream>
#include <cassert>

int get_change(int m) {
  int n = 0;
  if (m < 5){
    return m;
  }else if(m < 10){
    return (1 + m - 5);
  } else {
    return (m/10 + get_change(m % 10));
  }
  return n;
}

int test_get_change(){
  std::cout << "get_change(2)" << get_change(2) << std::endl;
  assert(get_change(2) == 2);
  std::cout << "get_change(4)" << get_change(4) << std::endl;
  assert(get_change(4) == 4);
  std::cout << "get_change(25)" << get_change(25) << std::endl;
  assert(get_change(25) == 3);
  std::cout << "get_change(100)" << get_change(100) << std::endl;
  assert(get_change(1000)== 100);
  std::cout << "get_change(28)" << get_change(28) << std::endl;
  assert(get_change(28)== 6);
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
  
  // test_get_change();
}
