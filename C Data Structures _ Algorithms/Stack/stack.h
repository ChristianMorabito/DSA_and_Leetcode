#ifndef STACK_H
#define STACK_H

typedef struct {
    size_t maxSize;
    int currSize;
    char* array;
    char (*pop)();
    void (*push)(char);
} Stack;

extern Stack stack;
void freeArray();
void mallocError();
void* push(char);
char pop();
void createStack();


#endif // STACK_H

