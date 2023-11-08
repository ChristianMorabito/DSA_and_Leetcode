#include <stdlib.h>
#include "queue.h"

void mallocError()
{
    printf("malloc error. Exiting...");
    exit(-1);
}

void printList()
{
    Node* curr = queue.head;
    while (curr)
    {
        printf("%c --> ", curr->value);
        curr = curr->next;
    }
    printf("NULL");

}

void freeList()
{
    Node* curr = queue.head;
    Node* holder = curr;
    while (curr)
    {
        curr = curr->next;
        free(holder);
        holder = curr;
    }
    queue.head = NULL;
}

void enqueue(char value)
{
    if (!queue.head)
    {
        queue.head = malloc(sizeof(Node));  // create first node
        if (!queue.head) mallocError();
        queue.tail = queue.head;
    }
    else
    {
        queue.tail->next = malloc(sizeof(Node));  // create node
        if (!queue.tail->next) mallocError();
        queue.tail = queue.tail->next;
    }

    queue.tail->value = value;
    queue.tail->next = NULL;
}

char dequeue()
{
    if (!queue.head) return '\0';
    char frontValue = queue.head->value;
    Node* tempHold = queue.head->next;
    free(queue.head);  // free node
    queue.head = tempHold;
    return frontValue;
}

void createQueue()
{
    // assign the methods to the queue struct
    queue.enqueue = enqueue;
    queue.dequeue = dequeue;
}

