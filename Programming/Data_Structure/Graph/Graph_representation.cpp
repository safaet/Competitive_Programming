#include<bits/stdc++.h>
using namespace std;

int main(){

	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif
		
	int n, e;
	cin>> n >> e;

	int adj[n+1][e+1];

	for(int i = 0; i<e; i++){
		int u, v;
		cin >> u >> v;
		adj[u][v] = 1;
		adj[v][u] = 1;
	}

	cout << adj[1][2];

	return 0;
}