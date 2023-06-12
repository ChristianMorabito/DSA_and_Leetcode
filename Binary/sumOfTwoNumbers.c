// Fuller adder in an algorithm

int main() {
  
  int a = 0b1010;
  int b = 0b1111;
  int carry;
  
  while (b != 0){
    carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
    
    
  }

  return 0;
}