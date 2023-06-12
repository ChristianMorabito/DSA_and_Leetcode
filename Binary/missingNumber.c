int main() {
  
  int nums[] = {0, 1, 2, 3, 5, 6, 7, 8, 9};
  int len = sizeof(nums) / sizeof(nums[0]);
  int result = 0;
  
  for (int i = 0; i < len; i++){
    result = result ^ (i+1) ^ nums[i]; // result = 4   
  }

  return 0;
}

