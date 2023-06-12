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
void merge(Node** dummy, Node* head, Node* head1) {
    *dummy = (Node* ) malloc(sizeof(Node));
    Node* tail = NULL;
    tail = *dummy;
    while (head && head1){
        if (head->value <= head1->value){
            tail->next = head;
            head = head->next;
        }
        else{
            tail->next = head1;
            head1 = head1->next;
        }
        tail = tail->next;
    }
    if (head){
        tail->next = head;
    }
    else{
        tail->next = head1;
    }

}

int main(){
    Node* head = NULL;
    Node* head1 = NULL;
    // list1
    append(&head, 0);
    append(&head, 5);
    append(&head1, 2);
    append(&head1, 7);
    // merge 2 sorted lists
    Node* dummy = NULL;
    merge(&dummy, head, head1);
    printL(dummy->next);

    return 0;
}

