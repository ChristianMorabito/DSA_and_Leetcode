#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int value;
    struct Node* next;
}Node;
void create(Node* head, int len){
    Node* current = head;
    for (int i = 0; i < len; i++){
        // CREATE NODE
        Node* node = NULL;
        node = (Node* ) malloc(sizeof(Node));
        node->value = i;
        // CONNECT NODE
        current->next = node;
        current = current->next;
    }
    current->next = NULL;
}
void printL(Node* head){
    Node* current = NULL;
    current = head;
    while (current){
        printf("[Node: %d] -> ", current->value);
        current = current->next;
    }
    printf("NULL");
    printf("\n");

}
void reorder(Node* head){
    Node* mid = NULL;
    Node* tail = NULL;
    mid = head;
    tail = head;
    // step 1) establish mid & tail pointers
    while (tail && tail->next){
        if (tail->next->next){
            tail = tail->next->next;
            mid = mid->next;
        }
        else{
            tail = tail->next;
        }
    }
    // step 2) reverse dir of right half & make mid->next = NULL
    Node* prev = mid;
    Node* curr = mid->next;
    Node* nxt = NULL;
    mid->next = NULL;
    // After loop: 0 -> 1 -> 2 <- 3 <- 4
    //                        ➘ NULL
    while (curr){
        nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    // step 3) while mid, reorder nodes
    Node* rNxtHold = NULL;
    Node* lNxtHold = NULL;
    Node* curL = head;
    Node* curR = tail;
    while (curL){
        lNxtHold = curL->next;
        rNxtHold = curR->next;
        curL->next = curR;
        curR->next = lNxtHold;
        curR = rNxtHold;
        curL = lNxtHold;

    }

}
int main(){
    // CREATE HEAD NODE
    Node head;
    create(&head, 3);
    printL(head.next);
    reorder(head.next);
    printL(head.next);
};