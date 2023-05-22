#include <iostream>
using namespace std;
int main() {
  int a = 10;
  int &r = a; // when declaring a reference variable you must initialize it at the same time
  r++; // updates the a variable since a is referenced with r as well

  // reference doesn't consume memory, it uses the same memory as a


  cout << a; // prints 11

  return 0;
}