#include <stdio.h>

int sort(int* array, int left, int right){
    int i = left;
    int j = right-1;
    int pivot = array[right];

    while (i < j){
        while (i < right && array[i] < pivot){
            i++;
        }
        while (j > left && array[j] >= pivot){
            j--;
        }
        if (i < j){
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;}
    }
    if (array[i] > pivot){
        int temp = array[i];
        array[i] = array[right];
        array[right] = temp;
    }
    return i;
}

void divide(int* array, int left, int right){
    if (left < right){
        int index = sort(array, left, right);
        divide(array, left, index - 1);
        divide(array, index + 1, right);}}

int main(){
    int array[] = {3,2,1,5,4,3,6,5,4,8,7,6,9,0};
    const int SIZE = sizeof(array) / sizeof(array[0]);
    divide(array, 0, SIZE - 1);
    // PRINT SORTED ARRAY
    for (int i = 0; i < SIZE; i++){
        printf("%d ", array[i]);
    }
    return 1;
}