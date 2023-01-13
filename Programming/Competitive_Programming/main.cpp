#include<bits/stdc++.h>
using namespace std;


int main()
{
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

	int n, a, b, i, x;

	vector<int> v;
	vector<int> :: iterator it;

	cin>>n;

	for(i = 0; i<n; i++){
		int m;
		cin>>m;
		v.push_back(m);
	}

	
	cin>>x >> a >> b;

	for(auto i= v.begin(); i != v.end(); i++){
		if(*i == x)
			v.erase(i);
	}

	for(auto i = v.begin(); i != v.end(); i++)
		cout<<*i<<" ";

	cout<<"Hello\n";

}