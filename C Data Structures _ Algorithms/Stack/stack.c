// stack data structure is designed to be created globally on stack memory.
// stack.array however is allocated onto the heap, so needs to be freed.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"
#define MAX_SIZE 10

void mallocError() {
    printf("malloc error. Exiting...");
    exit(-1);
}

void freeArray() {
    free(stack.array);
}

void* push(char item) {
    if (stack.currSize < stack.maxSize) {
        stack.array[stack.currSize] = item;
        stack.currSize++;
    }
    return NULL;
}

char pop() {
    if (stack.currSize == 0) return '\0';
    char poppedChar = stack.array[stack.currSize-1];
    stack.array[stack.currSize-1] = '\0';
    stack.currSize--;
    return poppedChar;
}

void createStack() {
    stack.array = malloc(sizeof(char) * MAX_SIZE+1);  // allocate memory for array within stack struct.
    memset(stack.array, '\0', sizeof(char) * MAX_SIZE+1);
    if (!stack.array) mallocError();
    stack.maxSize = MAX_SIZE;
    stack.currSize = 0;
    stack.push = push;
    stack.pop = pop;
}
