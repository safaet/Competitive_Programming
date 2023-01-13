#include <bits/stdc++.h>

using namespace std;

int main(){
    #ifndef ONLINE_JUDGE

        freopen("input.txt", "r", stdin);

        freopen("output.txt", "w", stdout);

    #endif

    int arr[100][100] = {0}, i, j;

    int n, m;
    cin>> n >> m;

    for(i = 0; i<m; i++) {
        int u, v;
        cin>> u>> v;

        arr[u][v] = 1;
        arr[v][u] = 1;
    }

    for(i = 0; i<n; i++) {
        for(j = 0; j<n; j++)
            cout<<arr[i][j]<<" ";
        cout<<endl;
    }
}