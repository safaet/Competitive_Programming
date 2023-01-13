#include <bits/stdc++.h>
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif
	vector<int> v;
	vector<int> :: iterator low, up;

	int n, q, a;

	cin >>n;

	for(int i = 0; i<n;i ++){
		int m;
		cin>>m;
		v.push_back(m);
	}

	cin>>q;

	for(int i = 0; i<q; i++){
		cin>>a;
		if(binary_search(v.begin(), v.end(), a)) {
			low = lower_bound(v.begin(), v.end(), a);
			cout<<"Yes "<<(low -v.begin()+1)<<endl;
		}
		else {
			up = upper_bound(v.begin(), v.end(), a);
			cout<<"No "<<(up -v.begin()+1)<<endl;
		}
	}
	
}