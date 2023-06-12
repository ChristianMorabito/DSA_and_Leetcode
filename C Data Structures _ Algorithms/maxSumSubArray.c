#include <stdio.h>

int max(int a, int b){
    return (a > b) ? a : b;
}
int maxSumSubArray(const int* array, int n){
    int localSum = array[0], maxSum = array[0], num;
    for (int i = 1; i < n; i++){
        num = array[i];
        localSum = max(localSum+(num), num);
        maxSum = max(localSum, maxSum);
    }
    return maxSum;
}
int main(){
    int array[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    const int N = sizeof(array) / sizeof(array[0]);
    printf("The max sum is: %d", maxSumSubArray(array, N));
}