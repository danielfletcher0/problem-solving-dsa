#include <iostream>
using namespace std;

struct Rectangle {
  int length;
  int height;
};
int main() {
  // int a = 10;
  // int *p; // Only use the asterick for pointer declaration and 
  //         // dereferencing (accessing value at the adress of the pointer)

  // p = &a; // '&' is used for accessing the address of the data variable

  // cout << "The value at the address of the pointe is " << *p << " but the adress is " << p << endl;

  // Pointer to an array


  // int A[5] = {2, 4, 6, 8, 10};

  // p = new int[5]; // alocates the array in the heap but the pointer is in the stack
  // p[0] = 10; p[1] = 20; p[2] = 30; p[3] = 40; p[4] = 50;
  // // p = A; // You don't have to use '&' when pointing to the address of an array
  //       // Because name of the array A itself is the starting address of the array

  // for (int i = 0; i < 5; i++) {

  //   cout << p[i] << endl; //acessing the array values using the pointer
  // }
  // delete [ ] p; // when you are done using the memory for the data you allocated you have to free 
  //             // it by using the delete keyword. We allocated space for an array so we should use the '[]' brackets

  int *p1;
  char *p2;
  float *p3;
  double *p4;

  struct Rectangle *r;
  r = new struct Rectangle;

  r-> length = 20;
  r-> height = 34;
  // struct Rectangle r = {10, 5};
  // struct Rectangle *p5 = &r;

  // cout << r.length << endl; // use '.' when using normal variables to access structure members
  // cout << r.height << endl;
  cout << r -> height << endl;
  cout << r -> length << endl;
  // cout << p5 -> height << endl; // use '->' when using pointers to access structure members
  // cout << p5 -> length << endl;

  // cout << sizeof(p1) << endl;
  // cout << sizeof(p2) << endl;
  // cout << sizeof(p3) << endl;
  // cout << sizeof(p4) << endl;
  // cout << sizeof(p5) << endl; // Every pointer takes the same amount of memory, it is independent
  //                             // of it's data type


  return 0;

  // When the program ends, the heap memory is automatically deleted


}