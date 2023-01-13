#include<bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int l, int r, int x){
	while(l <= r) {
		int m = l + (r-l) / 2;

		if(arr[m] == x)
			return m;
		if(arr[m] < x)
			l = m +1;
		else
			r = m-1;
	}

	return -1;
}

int main()
{
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif
		
		int i, ad;

		string str;

		while(cin>>str){

			int arr[200] = {0};

			int l = str.size();

			for(i = 0; i<l; i++){
				ad = str[i];

				arr[ad] = arr[ad] +1;
			}

			for(i = 30; i<200; i++){
				if(arr[i] != 0){
					cout<<i<<" "<<arr[i]<<endl;
				}
			}
			cout<<endl;
		}
}