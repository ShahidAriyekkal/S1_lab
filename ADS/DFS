#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

void dfs(int adj[MAX][MAX], int V, int s, bool visited[MAX]) {
    int i;
    printf("%d ", s);
    visited[s] = true;
    
    for (i = 0; i < V; i++) {
        if (adj[s][i] == 1 && !visited[i]) {
            dfs(adj, V, i, visited);
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
    
    bool visited[MAX] = {false};
    
    printf("DFS starting from 2:\n");
    dfs(adj, V, 2, visited);
    
    return 0;
}
