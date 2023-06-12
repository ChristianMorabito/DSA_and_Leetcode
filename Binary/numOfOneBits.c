int main() {
  
  int n = 11, result = 0;
  
  while (n){
    result += n % 2;
    n = n >> 1;
  }

  return 0;
}

