#include <bits/stdc++.h>
using namespace std;


void bubbleSort(int arr[], int x){
	int i, j, a = 0;

	for(i = 0; i< x; i++){
		for(j = 0; j< x-i-1; j++)
			if(arr[j] > arr[j+1]){
				a = a+1;
				swap(arr[j], arr[j+1]);
			}
	}
	cout<<"Optimal train swapping takes "<<a <<" swaps."<<endl;
}

void printArray(int arr[], int size){
	int i;

	for(i = 0; i<size; i++)
		cout<<arr[i]<<" ";
	cout<<endl;
}

int main(){

	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif
		
	int arr[100], n, t;

	cin>> t;
	while(t--){

		cin>>n;
	
			for(int i = 0; i<n; i++)
				cin>>arr[i];
	
			bubbleSort(arr, n);
		}
		return 0;
}