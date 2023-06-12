#include <stdlib.h>

void dynamicArray(int** array, int* n, int* filled, int num){
    if (!*array){ // One-time case to create & initialise array.
        *array = malloc(sizeof(int));
        *array[0] = num;
        (*n)++;
    }
    else if ((*filled)+1 < *n){ // if there is space in the memory block, then just add the num at the filled point.
        (*array)[*filled] = num;
    }
    else { // else, reallocate the array to a new memory block of double length.
        *array = realloc(*array, ((*n)*2)*sizeof(int));
        (*array)[*filled] = num;
        (*n)*=2;
    }
    (*filled)++;
}

int main(){
    int n = 0; // n = array size
    int filled = 0;
    int* ptr = NULL;
    dynamicArray(&ptr, &n, &filled, 0);
    dynamicArray(&ptr, &n, &filled, 1);
    dynamicArray(&ptr, &n, &filled, 2);

    return 0;
}
