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
    printf("NULL\n");
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
void removeNthLastNode(Node** dummy, Node* head, int n){
    *dummy = (Node* ) malloc(sizeof(Node));
    (*dummy)->next = head;
    Node* left = *dummy;
    Node* right = (*dummy)->next;
    while (right && n > 0){
        right = right->next;
        n--;
    }
    while (right){
        left = left->next;
        right = right->next;
    }
    left->next = left->next->next;
}

int main(){
    Node* head = NULL;
    // Linked List:
    append(&head, 1); append(&head, 2); append(&head, 3); append(&head, 4); append(&head, 5); append(&head, 6); append(&head, 7); append(&head, 8); append(&head, 9); append(&head, 10);
    // remove nth last node
    Node* dummy = NULL;
    removeNthLastNode(&dummy, head, 3);
    printL(dummy->next);
    return 0;
}