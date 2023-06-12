#include <stdio.h>
#include <string.h>

// PROTOTYPE FUNCTIONS
int insertionSort(int* array, int SIZE, int(* compare)(int* array, int, int));
int increase(int* array, int, int);
int decrease(int* array, int, int);
int printArr(int* array, int SIZE, int status);

// DRIVER FUNCTION
int main(){
    int status = 0;
    int array[] = {8, 0, 1, 7, 4, 6, 2, 3, 9, 5};
    const int SIZE = sizeof(array) / sizeof(array[0]);
    printArr(array, SIZE, status);  // UNSORTED
    status = insertionSort(array, SIZE, decrease);
    status = printArr(array, SIZE, status);  // SORTED

    return 0;
}
int insertionSort(int* array, int SIZE, int(* compare)(int* array, int, int)){
    int temp, j;
    for (int i = 1; i < SIZE; i++){
        temp = array[i];
        j = i-1;
        while (compare(array, j, temp)){
            array[j+1] = array[j];
            array[j] = temp;
            j--;
        }
    }
    return 1;
}
int increase(int* array, int j, int temp){
    return temp < array[j] && j > -1;
}
int decrease(int* array, int j, int temp){
    return temp > array[j] && j > -1;;
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

