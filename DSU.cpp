#include <bits/stdc++.h>
using namespace std;
class DSU{
public:
 vector<int>par;
 vector<int>rank;
 DSU(int n){
     par.resize(n+1);
     rank.resize(n+1);
     for(int i=1;i<=n;i++){
         par[i]=i;
         rank[i]=1;
     }
 }
 int get_leader(int u){
     if(par[u]==u){
         return u;
     }
     else{
         // path compression
         return par[u]=get_leader(par[u]);
     }
 }
 void merge(int u,int v){
     u=get_leader(u);
     v=get_leader(v);
     if(u==v){
         //case of cyle
         return;
     }
     else{
         if(rank[u]<rank[v]){
             swap(u,v);
         }
         par[v]=u;
         rank[u]+=rank[v];
     }
 }
};
class dsu{
    public:
    vector<int>par;
    dsu(int n){
        par.resize(n);
        for(int i=1;i<=n;i++){
            par[i]=-1;
        }
    }
    int get_leader(int u){
        if(par[u]<0){
            return u;
        }
        else{
            return par[u]=get_leader(par[u]);
        }
    }
    void merge(int u,int v){
        u=get_leader(u);
        v=get_leader(v);
        if(u==v){
            return;
        }
        else{
            //par[u]->-2 par[v]->-3
            if(par[u]>par[v]){
            swap(u,v);    
            }
            par[u]+=par[v];
            par[v]=u;
        }
    }
};
int main() {
    int n,m;
    // sorting -> weights
    //array -> edges
    for(int i=0;i<m;i++){
     //vec.push_back({wt,n1,n2})        
    }
    DSU d(n+1);
    //sort(vec)
    int fnodes=0;
    for(int i=0;i<m;i++){
        //vec[0]->wt vec[1]->n1 vec[2]->n2
        if(d.merge(n1,n2)){
            ans+=vec[0];
            fnodes++;
        }
    }
    if(fnode==n-1){
        //done
    }
    
    
    
    
}
