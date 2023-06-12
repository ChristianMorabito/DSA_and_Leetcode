#include <stdio.h>
#include <stdbool.h>

// bundling of function arguments into a struct.
typedef struct{
    int* arr;
    int N;
    int x;
}funcData;

int innerSearch(funcData package, bool searchFirst){
    int* arr = package.arr;
    int x = package.x;
    int low = 0, high = package.N, mid, result = -1;
    while (low <= high){
        mid = (low + high) / 2;
        if (arr[mid] == x){
            result = mid;
            if (searchFirst){
                high = mid-1; // Go on searching towards left (lower indices)
            }
            else{
                low = mid+1; // Go on searching towards right (higher indices)
            }
        }
        else if (x < arr[mid]){
            high = mid-1;
        }
        else {
            low = mid+1;
        }
    }
    return result;
}

int binarySearch(funcData package){
    int firstIndex = innerSearch(package, true);
    int lastIndex = innerSearch(package, false);
    return (lastIndex - firstIndex)+1;
}

int main(){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 7,
                 7, 7, 7, 8, 9, 10, 11 };
    const int N = sizeof(arr) / sizeof(arr[0]);

    // count the amount of 7s in the array.
    int num = 7;


    // bundling of function arguments into a struct.
    funcData package;
    package.arr = arr;
    package.N = N;
    package.x = num;

    // call the function & print result
    printf("The number %d appears %d times\n", num, binarySearch(package));
    return 0;
}