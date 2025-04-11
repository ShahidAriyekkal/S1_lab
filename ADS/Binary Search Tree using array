#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

int bst[MAX_SIZE];
int size = 0;

void initializeBST() {
    for (int i = 0; i < MAX_SIZE; i++) {
        bst[i] = -1;
    }
}

void insert(int value) {
    if (size == MAX_SIZE) {
        printf("BST is full!\n");
        return;
    }

    int index = 0;
    while (1) {
        if (bst[index] == -1) {
            bst[index] = value;
            size++;
            printf("%d inserted into BST.\n", value);
            return;
        }
        if (value < bst[index]) {
            index = 2 * index + 1;
        } else if (value > bst[index]) {
            index = 2 * index + 2;
        } else {
            printf("%d is already in the BST.\n", value);
            return;
        }
        if (index >= MAX_SIZE) {
            printf("Index out of bounds!\n");
            return;
        }
    }
}

int findMin(int index) {
    while (2 * index + 1 < MAX_SIZE && bst[2 * index + 1] != -1) {
        index = 2 * index + 1;
    }
    return index;
}

void delete(int value) {
    int index = 0, parent = -1;
    while (index < MAX_SIZE && bst[index] != -1) {
        if (value < bst[index]) {
            parent = index;
            index = 2 * index + 1;
        } else if (value > bst[index]) {
            parent = index;
            index = 2 * index + 2;
        } else {
            if (bst[2 * index + 1] == -1 && bst[2 * index + 2] == -1) {
                bst[index] = -1;
            } else if (bst[2 * index + 1] == -1 || bst[2 * index + 2] == -1) {
                int child = (bst[2 * index + 1] != -1) ? 2 * index + 1 : 2 * index + 2;
                bst[index] = bst[child];
                bst[child] = -1;
            } else {
                int minIndex = findMin(2 * index + 2);
                bst[index] = bst[minIndex];
                delete(bst[minIndex]);
            }
            printf("%d deleted from BST.\n", value);
            size--;
            return;
        }
    }
    printf("%d not found in BST.\n", value);
}

void inorderTraversal(int index) {
    if (index >= MAX_SIZE || bst[index] == -1) return;
    inorderTraversal(2 * index + 1);
    printf("%d ", bst[index]);
    inorderTraversal(2 * index + 2);
}

int main() {
    int choice, value;

    initializeBST();

    while (1) {
        printf("\nMenu:\n");
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. In-order Traversal\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(value);
                break;
            case 2:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                delete(value);
                break;
            case 3:
                printf("In-order Traversal: ");
                inorderTraversal(0);
                printf("\n");
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
