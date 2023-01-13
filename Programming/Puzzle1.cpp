#include<bits/stdc++.h>
using namespace std;

void getGroupOfArrays(int arr[], int n){

	int i, j;

	for(i = 1; i<=5; i = i+1){
		if(i%n != 0)
			cout << arr[i]<<" ";
		else if (i%n == 0)
			cout<<arr[i]<<",";
	}
	cout<<endl;
}

int main()
{
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

	int arr[99999],n;

	for(int i = 1; i<=5; i++){
		cin>>arr[i];
	}

	cin>>n;

	getGroupOfArrays(arr, n);
	
}