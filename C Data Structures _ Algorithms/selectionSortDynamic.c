#include <stdio.h>
#include <string.h>

// PROTOTYPE FUNCTIONS
int selectionSort(int* array, int SIZE, int(* compare)(int* array, int, int));
int increase(int* array, int, int);
int decrease(int* array, int, int);
int printArr(int* array, int SIZE, int status);

// DRIVER FUNCTION
int main(){
    int status = 0;
    int array[] = {8, 0, 1, 7, 4, 6, 2, 3, 9, 5};
    const int SIZE = sizeof(array) / sizeof(array[0]);
    printArr(array, SIZE, status);  // UNSORTED
    status = selectionSort(array, SIZE, increase);
    status = printArr(array, SIZE, status);  // SORTED
    return 0;
}
int selectionSort(int* array, int SIZE, int(* compare)(int* array, int, int)){
    int minIndex;
    for (int i = 0; i < SIZE; i++){
        minIndex = i;
        for (int j = i+1; j < SIZE; j++){
            minIndex = compare(array, minIndex, j);
        }
        if (i != minIndex){
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }
    return 1;
}
int increase(int* array, int minIndex, int j){
    if (array[j] < array[minIndex]){
        minIndex = j;
    }
    return minIndex;
}
int decrease(int* array, int minIndex, int j){
    if (array[j] > array[minIndex]){
        minIndex = j;
    }
    return minIndex;
}
int printArr(int* array, int SIZE, int status){
    char strStatus[] = "Unsorted";
    if (status){
        strcpy(strStatus, "Sorted");
    }
    printf("%s: ", strStatus);
    for (int i = 0; i < SIZE-1; i++){
        printf("%d, ", array[i]);
    }
    printf("%d\n", array[SIZE-1]);
    return 0;
}