#include <string.h>
#include <stdio.h>

// PROTOTYPE FUNCTIONS
int bubbleSort(int* array, int SIZE, int(*comp)(int, int));
int printArr(int* array, int SIZE, int status);
int lowToHigh(int, int);
int highToLow(int, int);

// DRIVER CODE
int main() {
    int status = 0;
    int array[] = {12, 11, 13, 5, 6, 7};
    const int SIZE = sizeof(array) / sizeof(array[0]);

    printArr(array, SIZE, status);  // PRINT UNSORTED
    bubbleSort(array, SIZE, lowToHigh); // increasing order
    status = printArr(array, SIZE, status);  // PRINT SORTED & status is changed back to False
    return 0;
}
int bubbleSort(int* array, int SIZE, int(*comp)(int, int)){
    for (int i = 0; i < SIZE-1; i++){
        for (int j = 0; j < (SIZE - i)-1; j++){
            // if True, perform swap
            if (comp(array[j], array[j+1])){
                // swap
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    return 1;
}
int lowToHigh(int a, int b){ // RETURN TRUE OR FALSE
    return a < b;
}
int highToLow(int a, int b){ // RETURN TRUE OR FALSE
    return b < a;
}
int printArr(int* array, int SIZE, int status){
    char strStatus[10] = {"UNSORTED"};
    if (status){
        strcpy(strStatus, "SORTED");
    }
    printf("%s ARRAY: ", strStatus);
    for (int i = 0; i < SIZE-1; i++){
        printf("%d, ", array[i]);
    }
    printf("%d\n", array[SIZE-1]);
    return 0;
}