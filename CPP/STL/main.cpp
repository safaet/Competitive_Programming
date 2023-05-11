#include <bits/stdc++.h>
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

	vector<int> v;

	int n, y, a, b;

	cin>>n;

	for(int i = 0; i<n; i++){
		int m;
		cin>>m;
		v.push_back(m);
	}

	cin>>y>>a>>b;


	v.erase(v.begin()+(y-1));
	v.erase(v.begin()+(a-1), v.begin()+(b-1));

	cout<<v.size()<<endl;

	for(auto &j:v)
		cout<<j<<" ";
}