#include<bits/stdc++.h>
using namespace std;
void bfs(int src,vector<bool>&vis,vector<vector<int>>&adj,vector<int>&dis){
    queue<int>q;
    q.push(src);
    dis[src]=0;
    vis[src]=true;
    while(!q.empty()){
        int u =q.front();
        q.pop();
        for(auto x:adj[u]){
            if(vis[x]==false){
                q.push(x);
                dis[x]=dis[u]+1;
                vis[x]=true;
            }
        }
    }
}

bool bfs_cycle(int src,vector<bool>&vis,vector<vector<int>>&adj,vector<int>&par){
    queue<int>q;
    q.push(src);
    par[src]=-1;
    while(!q.empty()){
        int u =q.front();
        q.pop();
        for(auto x:adj[u]){
            if(vis[x]==false){
                q.push(x);
                par[x]=u;
                vis[x]=true;
            }
            else{
                if(x!=par[u]){
                    return true;
                }
            }
        }
    }
    return false;
}
bool cycle(vector<vector<int>>&adj){
    int n=adj.size();
    vector<bool>vis(adj.size(),false);
    vector<int>par(adj.size(),0);
    bool cycle_there=false;
    for(int i=1;i<n;i++){
        if(vis[i]==false){
            if(bfs_cycle(i,vis,adj,par)){
                cycle_there=true;
            }
        }
    }
    return cycle_there;
}
int component(vector<vector<int>>&adj){
    int n=adj.size();
    vector<bool>vis(adj.size(),false);
    int cnt=0;
    vector<int>dis(n,0);
    for(int i=1;i<n;i++){
        if(vis[i]==false){
            cnt++;
            bfs(i,vis,adj,dis);
        }
    }
    return cnt;
}
void nodes_on_minpath(int src,int des,vector<vector<int>>&adj){
    vector<bool>vis(adj.size(),false);
    vector<bool>vis1(adj.size(),false);
    vector<int>dis(adj.size(),0);
    vector<int>dis1(adj.size(),0);
    bfs(src,vis,adj,dis);
    bfs(des,vis1,adj,dis1);
    cout<<src<<" "<<des<<"\n";
    int n=adj.size();
    for(int i=1;i<n;i++){
        if(dis[i]+dis1[i]==dis[des]){
           cout<<i<<" ";
        }
    }
    cout<<"\n";
}
int main(){
    int n,m;
    cin >>n>>m;
    vector<vector<int>>adj(n+1);
    for(int i=0;i<m;i++){
        int x,y;
        cin >>x>>y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    queue<int>q;
    vector<bool>vis(n+1,false);
    int src;
    cin >> src;
    q.push(src);
    vis[src]=true;
    vector<int>dis(n+1,0);
    vector<int>par(n+1,0);
    dis[src]=0;
    par[src]=-1;
    while(!q.empty()){
        int u=q.front();
        cout<<u<<" ";
        q.pop();
        for(auto x:adj[u]){
            if(vis[x]==false){
                q.push(x);
                par[x]=u;
                dis[x]=dis[u]+1;
                vis[x]=true;
            }
        }
    }
    cout<<"\n";
    for(int i=1;i<=n;i++){
        cout<<dis[i]<<" ";
    }
    cout<<"\n";
    int des;
    cin >> des;
    int st_des=des;
    while(des!=-1){
        cout<<des<<" ";
        des=par[des];
    }
    cout<<"\n";
    des=st_des;
    cout<<component(adj)<<"\n";
    if(cycle(adj)){
        cout<<"Cycle in Graph detected\n";
    }
    else{
        cout<<"No cycle\n";
    }
    nodes_on_minpath(src,des,adj);
}
