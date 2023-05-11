#include <bits/stdc++.h>
using namespace std;

void showlist(list<int> g)
{
	list<int> :: iterator it;

	for(it = g.begin(); it != g.end(); it++)
		cout<<'\t'<<*it;
	cout<<"\n";
}

int main(){
	#ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

	
	list<int> gqlist1, gqlist2;

	for(int i = 0; i<10; i++){
		gqlist1.push_back(i*2);
		gqlist2.push_back(i*3);
	}

	cout<<"\nList 1 (gqlist1) is: ";
	showlist(gqlist1);

}