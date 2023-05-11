#include <bits/stdc++.h>
using namespace std;

vector<int> ar[10000];
vector<bool> vis(10000, false);

//int vis[10]={0};

void dfs(int v) {
    vis[v] = true;
    cout << v<<" -> ";

    for(int i = 0; i<ar[v].size(); i++) {
        int child = ar[v][i];
        if(vis[child] == false)
            dfs(child);
    }
}

int main(){
    #ifndef ONLINE_JUDGE

        freopen("input.txt", "r", stdin);

        freopen("output.txt", "w", stdout);

    #endif

        int n, e;

        cin>> n>> e;

        for(int i = 1; i<=e; i++)
            {
                int a, b;
                cin>> a >> b;
                ar[a].push_back(b);
                ar[b].push_back(a);
            }

        for(int i = 1; i<= n; i++) {
            cout << "Elements at index " << i << ": ";

            for(auto it = ar[i].begin(); it != ar[i].end(); it++) {
                cout << *it <<' ';
            }
            cout << endl;
        }

       dfs(1);

        //cout<<ar[1][1];

       /* int cc_count = 0;

        for(int i=0; i<n; i++)
            if (vis[i] == false) {
                dfs(i);
                cc_count++;
            }

        cout <<cc_count <<endl; */
        
        return 0;
   
}