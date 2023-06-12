#include <stdio.h>
#include <string.h>

// PROTOTYPE FUNCTIONS
int divide(int* array, int SIZE, int left, int right, int(* compare)(int, int));
void conquer(int* array, int left, int mid, int right, int(* compare)(int, int));
int printArr(int* array, int SIZE, int status);
int increase(int a, int b);
int decrease(int a, int b);

// DRIVER FUNCTION
int main(){
    int array[] = {9, 5, 7, 0, 1, 3, 6, 5, 2, 4, 8};
    const int SIZE = sizeof(array) / sizeof(array[0]);
    int status = 0;  // status is False

    printArr(array, SIZE, status);  // PRINT UNSORTED
    status = divide(array, SIZE, 0, SIZE-1, increase); // status is True
    status = printArr(array, SIZE, status);  // PRINT SORTED & status is changed back to False
}

void conquer(int* array, int left, int mid, int right, int(* compare)(int a, int b)){
    // CREATE TEMP ARRAY SIZES (one array for left-side & one for right-side)
    int lSize = (mid - left) + 1;
    int rSize = right - mid;

    // CREATE EMPTY TEMP ARRAYS
    int lTemp[lSize], rTemp[rSize];

    // FILL LEFT TEMP ARRAY
    for (int i = 0; i < lSize; i++){
        lTemp[i] = array[i + left];
    }
    // FILL RIGHT TEMP ARRAY
    for (int j = 0; j < rSize; j++){
        rTemp[j] = array[mid + 1 + j];
    }
    // SORT LEFT & RIGHT TEMP ARRAYS
    int i = 0; // used to iterate the temp-left array
    int j = 0; // used to iterate the temp-right array
    int k = left; // used to iterate the global array
    while (i < lSize && j < rSize){
        if (compare(lTemp[i], rTemp[j])){
            array[k] = lTemp[i];
            i++;
        }
        else {
            array[k] = rTemp[j];
            j++;
        }
        k++;
    }
    while (i < lSize){
        array[k] = lTemp[i];
        i++;
        k++;
    }
    while (j < rSize){
        array[k] = rTemp[j];
        j++;
        k++;
    }
}
int divide(int* array, int SIZE, int left, int right, int(* compare)(int a, int b)){
    if (left < right){

        int mid = (left + right) / 2;

        // LEFT-SIDE recursive divide
        divide(array, SIZE, left, mid, compare);
        // RIGHT-SIDE recursive divide
        divide(array, SIZE, mid+1, right, compare);

        // SORT function
        conquer(array, left, mid, right, compare);

    }
    return 1;
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
int increase(int a, int b){
    return a < b;
}
int decrease(int a, int b){
    return b < a;
}