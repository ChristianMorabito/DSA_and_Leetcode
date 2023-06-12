#include <stdio.h>

// PROTOTYPE FUNCTIONS
void printIndex(const int* guess, int index);
int binarySearch(const int* array, const int* guess, int low, int high);

// DRIVER CODE
int main() {
    int guess;
    printf("Enter a number between 150 & 159:\n");
    scanf("%d", &guess);
    const int array[] = {150, 151, 152, 153, 154, 155, 156, 157, 158, 159};
    const int SIZE = sizeof(array) / sizeof(array[0]);

    // BINARY SEARCH FUNCTION - recursive
    int low = 0;
    int high = SIZE-1;
    int index = binarySearch(array, &guess, low, high);
    printIndex(&guess, index);
    return 0;
}

void printIndex(const int* guess, int index){
    if (index == -1){
        printf("Invalid number guessed.\n");
    }
    else {
        printf("Index is %d", index);
    }
}
int binarySearch(const int* array, const int* guess, int low, int high){

    if (low > high) {
        return -1;
    }
        int mid = (low + high) / 2;
        if (*guess == array[mid]){
            return mid;
        }
        if (*guess < array[mid]){
            return binarySearch(array, guess, low, mid-1);
        }
        else {
            return binarySearch(array, guess, mid+1, high);
        }

}