#include <stdio.h>

typedef struct{
    int min;
    int max;
}values;

values minMax(const int* nums, int SIZE){
    values comp;
    comp.min = nums[0]; comp.max = nums[0];
    for (int i = 1; i < SIZE; i++){
        if (nums[i] < comp.min){
            comp.min = nums[i];
        }
        if (nums[i] > comp.max){
            comp.max = nums[i];
        }
    }
    return comp;
}

int main(){
    int nums[] = {4, 32, 65, 1,90, 6,65};
    const int SIZE = sizeof(nums) / sizeof(nums[0]);
    values comp = minMax(nums, SIZE);
    printf("min num is: %d\nmax num is: %d", comp.min, comp.max);
    return 0;
}