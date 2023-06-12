#include <stdlib.h>
#include <stdio.h>

typedef struct Node{
    int value;
    struct Node* next;
}Node;
void printL(Node* head){
    Node* current = NULL;
    current = head;
    printf("LINKED LIST: ");
    while (current){
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("-> NULL");
}
void append(Node** head, int value){
    // Create Node & fill it
    Node* node = NULL;
    node = (Node* ) malloc(sizeof(Node));
    node->next = NULL;
    node->value = value;

    Node* curr = NULL;
    if (*head){
        curr = *head;
        while (curr->next){
            curr = curr->next;
        }
        curr->next = node;
    }
    else {
        *head = node;
    }
}
void reverse(Node** head){
    Node* current = *head;
    Node* prev = NULL;
    Node* next = NULL;

    while (current){
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}
int main(){
    Node* head = NULL;
    append(&head, 0);
    append(&head, 5);
    append(&head, 10);
    append(&head, 15);
    append(&head, 20);
    printL(head);
    reverse(&head);
    printf("\nREVERSED ");
    printL(head);

    return 0;
}

