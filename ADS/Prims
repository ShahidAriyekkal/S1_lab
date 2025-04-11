#include <stdio.h>
#include <limits.h>
#include<stdbool.h>

#define MAX 100

int minKey(int key[], bool mstSet[], int V) {
    int min = INT_MAX, minIndex,v;
    for (v = 0; v < V; v++) {
        if (!mstSet[v] && key[v] < min) {
            min = key[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void primMST(int adj[MAX][MAX], int V) {
    int parent[V],i,count,u,v;
    int key[V];
    bool mstSet[V];
    for (i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
        parent[i] = -1;
    }
    key[0] = 0;
    for (count = 0; count < V - 1; count++) {
        u = minKey(key, mstSet, V);
        mstSet[u] = true;
        for (v = 0; v < V; v++) {
            if (adj[u][v] != 0 && !mstSet[v] && adj[u][v] < key[v]) {
                key[v] = adj[u][v];
                parent[v] = u;
            }
        }
    }
    printf("Edge \tWeight\n");
    for (i = 1; i < V; i++) {
        printf("%d - %d \t%d\n", parent[i], i, adj[i][parent[i]]);
    }
}

void addEdge(int adj[MAX][MAX], int u, int v, int weight) {
    adj[u][v] = weight;
    adj[v][u] = weight;
}

int main() {
    int V = 5;
    int adj[MAX][MAX] = {0};
    addEdge(adj, 0, 1, 2);
    addEdge(adj, 0, 3, 6);
    addEdge(adj, 1, 2, 3);
    addEdge(adj, 1, 3, 8);
    addEdge(adj, 1, 4, 5);
    addEdge(adj, 2, 4, 7);
    addEdge(adj, 3, 4, 9);
    printf("Minimum Spanning Tree (MST) using Prim's Algorithm:\n");
    primMST(adj, V);
    return 0;
}
