#include <bits/stdc++.h>
using namespace std;

#define pb push_back

vector<bool> v;
vector<vector<int>> g;

void edge(int a, int b)
{
    g[a].pb(b);
}

void bfs(int u)
{
    queue<int> q;

    q.push(u);
    v[u] = true;

    while (!q.empty())
    {
        int f = q.front();
        q.pop();

        cout << f << " ";

        for (auto i = g[f].begin(); i != g[f].end(); i++)
        {
            if (!v[*i])
            {
                q.push(*i);
                v[*i] = true;
            }
        }
    }
}

int main()
{

    #ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif
    
    int t, n;

    cin>>t;
    while(t--){

    	v.assign(n, false);
    	g.assign(n, vector<int> ());

    	cin>>n;
    	int arr[n+2];

    	for(int i = 1; i<=n; i++)
    		cin>> arr[i];

    	for(int i = 1; i<=(2*n-1); i++){
    		if(arr[i] == 0)
    			edge(i, n+1);
    		else
    			edge(n+1, i);
    	}
    	bfs(n);
    }
}