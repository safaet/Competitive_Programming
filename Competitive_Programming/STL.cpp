#include <bits/stdc++.h>

using namespace std;

ostream_iterator<int> printit(cout, " ");

#define ROW 4
#define COL 5
#define pb push_back

vector<bool> v;
vector<vector<int> > g;

void edge(int a, int b) {
    g[a].pb(b);
    //g[b].pb(a);
}

void bfs(int u) {
    queue<int> q;

    q.push(u);
    v[u] = true;

    while(!q.empty()) {
        int f = q.front();
        q.pop();

        cout<< f<< " ";

        for(auto i = g[f].begin(); i != g[f].end(); i++) {
            if(!v[*i]) {
                q.push(*i);
                v[*i] = true;
            }
        }
    }
}

int main(){
    #ifndef ONLINE_JUDGE

        freopen("input.txt", "r", stdin);

        freopen("output.txt", "w", stdout);

    #endif

    int n, m;
    vector<int> v[n+1];

    cin>>n >> m;

    
}