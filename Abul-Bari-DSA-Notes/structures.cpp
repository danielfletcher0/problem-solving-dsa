#include <iostream>
using namespace std;


struct Rectangle { // inside structures, pairing is done (allocating memory to data members)
  
  int length;
  int height;
  char x; //allocates 4 bytes but uses 1 byte


}; //r2, r3, r4. can also declare it here before the semicolon.
// definition doesn't consume memory until you declare a variable of its type

// struct Rectangle r2, r3, r4; // Global declarations of the structure


int main() {
  struct Rectangle r;
  // struct Rectangle r = {12, 11} can also initialize like this

  r.length = 12;
  r.height = 11;

  int area = r.length * r.height;

  cout << area << " of structure with size of " << sizeof(r);


  return 0;
}