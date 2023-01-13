#include <bits/stdc++.h>
using namespace std;

vector<int> ar[100001];
vector<bool> vis(100001, false);

void dfs(int v) {
    vis[v] = true;
    //cout<<"dfs call = "<<endl;
   
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
    

        int n, e, t;

        cin>> t;

        while(t--){

            cin>> n>> e;

            for(int i = 0; i<e; i++)
                {
                    int a, b;
                    cin>> a >> b;
                    ar[a].push_back(b);
                    ar[b].push_back(a);
                }

            int cc_count = 0;

            for(int i = 0; i<n; i++)
                //cout<<"vis = "<<vis[i]<<endl;

            for(int i=0; i<n; i++){
                if (vis[i] == false) {
                    dfs(i);
                    cc_count = cc_count+1;
                }
            }

            cout <<cc_count <<endl;

            for(int i = 0; i< n; i++) {
            cout << "Elements at index " << i << ": ";

            for(auto it = ar[i].begin(); it != ar[i].end(); it++) {
                cout << *it <<' ';
            }
            cout << endl;
        }

            for(int i =0; i<=n; i++)
                vis[i] = false;

    }
        
        return 0;
   
}