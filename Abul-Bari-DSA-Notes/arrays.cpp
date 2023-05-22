#include <iostream>
using namespace std;


int main() {
  // int A[5]; for declaring arrays
  // A[0] = 12;
  // A[1] = 15;
  // A[2] = 25;

  // int A[5] = {2, 4, 6, 8, 10}; //also works

  // cout << sizeof(A) << endl; // integers take 4 bytes
  // cout << A[1] << endl;
  int n;
  cout << "Enter the size of the array" << endl;
  cin >> n;
  int A[n] = {2, 4, 6, 8, 10, 12, 14}; // variable sized array
  // int A[10] = {2, 4, 6, 8, 10, 12, 14};
  cout << sizeof(A) << endl; // integers take 4 bytes
  cout << A[8] << endl;
  cout << A[9] << endl;
  // the locations in the array where you didn't initialize a value gets a value of 0 by default

  // for (int i = 0; i < 10; i++) { // Give constant value for the size of an array (good practice)
  //   cout << A[i] << endl;
  // }

  for (int x:A) {
    cout << x << endl;
  }

  return 0;
}