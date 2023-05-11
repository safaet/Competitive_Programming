#include <bits/stdc++.h>
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

	set<int> a;

	int n, x, y;

	cin>>n;

	while(n--){
		cin>> y>>x;

		if(y == 1)
			a.insert(x);
		else if(y == 2)
			a.erase(x);
		else if(y == 3) {
			auto pos = a.find(x);
			if(pos != a.end())
				cout<<"Yes\n";
			else
				cout<<"No\n";
		}
	}
}