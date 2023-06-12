#include <stdlib.h>
#define N 3

typedef struct Node{
    int endWord;
    struct Node* children[N];
}Node;
Node* create(){
    Node* head = (Node* )malloc(sizeof(Node));
    for (int i=0; i < N; i++){
        head->children[i] = NULL;
    }
    head->endWord = 0;
    return head;
}
int hasChildren(Node* node){
    for (int i = 0; i < N; i++){
        if (node->children[i]){
            return 1;
        }
    }
    return 0;
}
void insert(Node** head, char* str){
    Node* cur = NULL;
    if (!*head) *head = create();
    cur = *head;
    while (*str){
        if (!cur->children[*str - 'a']){
            cur->children[*str - 'a'] = create();
        }
        cur = cur->children[*str - 'a'];
        str++;
    }
    cur->endWord = 1;
}
int _deleteRec(Node** head, char* str){
    if (!*str){
        (*head)->endWord = 0;
        return hasChildren(*head) == 0;
    }
    int nextDel = _deleteRec(&(*head)->children[*str - 'a'], str+1);
    if (nextDel){
        free((*head)->children[*str - 'a']);
        (*head)->children[*str - 'a'] = NULL;
    }
    return nextDel && !(*head)->endWord && !(hasChildren(*head));
}
int delete(Node** head, char* str){
    int result = _deleteRec(head, str);
    if (!hasChildren(*head)) *head = NULL;
    return result;
}
int main(){
    Node* head = NULL;
    insert(&head, "aa");
    insert(&head, "ab");
    delete(&head, "aa");

    return 0;
}