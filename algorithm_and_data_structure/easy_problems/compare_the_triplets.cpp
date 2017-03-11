/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Fri, 10th Feb 2017, T 11:31 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: compare-the-triplets.cpp
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 11:48 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
* 
* @problem link: https://www.hackerrank.com/challenges/compare-the-triplets
*/



#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int a[3];
  int b[3];

  int a_result = 0;
  int b_result = 0;

  for (int l = 0; l < 3; l++){
    cin >> a[l];
  }

  for (int k = 0; k < 3; k++){
    cin >> b[k];
  }

  for (int i = 0; i <= 3; i++){
    if (a[i] > b[i])
      a_result ++;
    if (b[i] > a[i])
      b_result ++;
  }

  cout << a_result << " " << b_result;

  return 0;
}
