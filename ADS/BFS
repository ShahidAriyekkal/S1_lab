#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

void bfs(int adj[MAX][MAX], int V, int s) {
    int q[MAX], front = 0, rear = 0,i,curr;    
    bool visited[MAX] = { false };
    visited[s] = true;
    q[rear++] = s;
    
    while (front < rear) {
        curr = q[front++];
        printf("%d ", curr);
        
        for (i = 0; i <=V; i++) {
            if (adj[curr][i] == 1 && !visited[i]) {
                visited[i] = true;
                q[rear++] = i;
            }
        }
    }
}

void addEdge(int adj[MAX][MAX], int u, int v) {
    adj[u][v] = 1;
    adj[v][u] = 1;
}

int main() {
    int V = 5;
    int adj[MAX][MAX] = {0};
    
    addEdge(adj, 1, 2);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);
    addEdge(adj, 4, 1);
    addEdge(adj, 2, 4);
    
    printf("BFS starting from 0:\n");
    bfs(adj, V, 2);
    
    return 0;
}
