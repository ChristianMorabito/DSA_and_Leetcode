#ifndef QUEUE_H
#define QUEUE_H

#include <stdio.h>

typedef struct Node {
    char value;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
    Node* tail;
    char (*dequeue)();
    void (*enqueue)(char);
} Queue;

extern Queue queue;  // queue is to be created in main.c global scope

void printList();
void freeList();
void mallocError();
void createQueue();
char dequeue();
void enqueue(char value);

#endif  // QUEUE_H
