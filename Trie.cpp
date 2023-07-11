#include<bits/stdc++.h>
using namespace std;
const int alph =26;
const int maxn=100000;
struct Trie{
    int trie[maxn][alph], nc, hot_nodes[maxn];
    int max_depth;
    void init(){
        for(int i=0;i<maxn;i++){
            for(int j=0;j<alph;j++){
                trie[i][j]=-1;
            }
        }
        nc=0;
        max_depth=0;
        for(int i=0;i<maxn;i++){
            hot_nodes[i]=0;
        }
    }
    void insert(string s){
        int cur=0;
        for(int i=0;i<s.length();i++){
            int c=s[i]-'a';
            if(trie[cur][c]==-1){
                trie[cur][c]=++nc;
            }
            cur=trie[cur][c];
        }
        hot_nodes[cur]++;
    }
    bool exact_check(string s){
        int cur=0;
        for(int i=0;i<s.length();i++){
            int c=s[i]-'a';
            if(trie[cur][c]==-1){
                return false;
            }
            cur=trie[cur][c];
        }
        if(hot_nodes[cur]>0){
            return true;
        }
        else{
            return false;
        }
    }
    bool prefix_check(string s){
        int cur=0;
        for(int i=0;i<s.length();i++){
            int c=s[i]-'a';
            if(trie[cur][c]==-1){
                return false;
            }
            cur=trie[cur][c];
        }
        return true;
    }
    int longest_prefix(){
        dfs(0,0);
    }
    int dfs(int n,int depth){
        int sum=hot_nodes[n];
        for(int i=0;i<26;i++){
            if(trie[n][i]!=-1){
                sum+=dfs(trie[n][i],depth+1);
            }
        }
        if(sum>=2&&depth>max_depth){
        max_depth=depth;
        }
        return sum;
    }
}
int main(){
    
}


