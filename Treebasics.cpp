#include<bits/stdc++.h>
using namespace std;
class node{
    public:
    int data;
    node* left;
    node* right;
    node(int d){
        data=d;
        left=NULL;
        right=NULL;
    }
};
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
struct Node
{
    int data;
    Node* left;
    Node* right;
};
node* buildtree(){
    int d;
    cin >> d;
    //base case
    if(d==-1){
        return NULL;
    }
    node* root = new node(d);
    root->left=buildtree();
    root->right=buildtree();
    return root;
}
void inorder(node* root){
    if(root==NULL){
        return;
    }
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
}
void postorder(node* root){
    if(root==NULL){
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout<<root->data<<" ";
}
void preorder(node* root){
    if(root==NULL){
        return;
    }
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right);
}
int height(node* root){
    //basecase -> null tree 
    if(root==NULL){
        return 0;
    }
    int ls=height(root->left);
    int rs=height(root->right);
    return 1+max(ls,rs);
}
void level(int cur,node* root){
    if(cur==0){
        cout<<root->data<<" ";
        return;
    }
    level(cur-1,root->left);
    level(cur-1,root->right);
}
void levelorder(node* root){
    queue<node*>q;
    q.push(root);
    while(!q.empty()){
        int n=q.size();
        for(int i=0;i<n;i++){
        node* cur_root=q.front();
        q.pop();
        if(cur_root!=NULL){
            cout<<cur_root->data<<" ";
            q.push(cur_root->left);
            q.push(cur_root->right);
        }
        }
        cout<<"\n";
    }
}
int countnodes(node* root){
    if(root==NULL){
        return 0;
    }
    int cnt=1;
    cnt+=countnodes(root->left);
    cnt+=countnodes(root->right);
    return cnt;
}
int sumnodes(node* root){
    if(root==NULL){
        return 0;
    }
    int sum=root->data;
    sum+=sumnodes(root->left);
    sum+=sumnodes(root->right);
    return sum;
}
vector<int> leftView(Node *root)
{
   // Your code here
   vector<int>ans;
   if(root==NULL){
       return ans;
   }
   queue<Node*>q;
   q.push(root);
   while(!q.empty()){
       int n=q.size();
       for(int i=0;i<n;i++){
        Node* cur=q.front();
        q.pop();
        if(i==0){
            ans.push_back(cur->data);
        }
        if(cur->left!=NULL){
            q.push(cur->left);
        }
        if(cur->right!=NULL){
            q.push(cur->right);
        }
       }
   }
   return ans;
}
void preorder_leftview(vector<int>&ans,Node* root,int level,int &max_level){
    if(root==NULL){
        return ;
    }
    if(level>max_level){
        ans.push_back(root->data);
        max_level=level;
    }
    preorder_leftview(ans,root->left,level+1,max_level);
    preorder_leftview(ans,root->right,level+1,max_level);
}
 vector<int> rightView(Node *root)
    {
       // Your code here
   vector<int>ans;
   if(root==NULL){
       return ans;
   }
   queue<Node*>q;
   q.push(root);
   while(!q.empty()){
       int n=q.size();
       for(int i=0;i<n;i++){
        Node* cur=q.front();
        q.pop();
        if(i==n-1){
            ans.push_back(cur->data);
        }
        if(cur->left!=NULL){
            q.push(cur->left);
        }
        if(cur->right!=NULL){
            q.push(cur->right);
        }
       }
   }
   return ans;
    }
vector<int> topView(Node *root){
        vector<int>ans;
        if(root==NULL){
            return ans;
        }
        map<int,int>mp;
        //at dis=d first node to be visible;
        queue<pair<Node*,int>>q;
        q.push({root,0});
        while(!q.empty()){
            Node* cur=q.front().first;
            int dis=q.front().second;
            q.pop();
            if(cur==NULL){
                continue;
            }
            if(mp.find(dis)==mp.end()){
                mp[dis]=cur->data;
            }
                q.push({cur->left,dis-1});
                q.push({cur->right,dis+1});
        }
        for(auto x:mp){
            ans.push_back(x.second);
        }
        return ans;
}
vector<int> bottomView(Node *root)
    {
        vector<int>ans;
        if(root==NULL){
            return ans;
        }
        map<int,int>mp;
        //at dis=d first node to be visible;
        queue<pair<Node*,int>>q;
        q.push({root,0});
        while(!q.empty()){
            Node* cur=q.front().first;
            int dis=q.front().second;
            q.pop();
            if(cur==NULL){
                continue;
            }
                mp[dis]=cur->data;
                q.push({cur->left,dis-1});
                q.push({cur->right,dis+1});
        }
        for(auto x:mp){
            ans.push_back(x.second);
        }
        return ans;
    }
TreeNode* invertTree(TreeNode* root) {
     if(root!=NULL){
      TreeNode* temp=root->left;
     root->left=root->right;
     root->right=temp;
     invertTree(root->left);
     invertTree(root->right);   
     }
     return root;
}
int diameter(node* root,int &max_dia){
    if(root==NULL){
        return 0;
    }
    int c_left=diameter(root->left,max_dia);
    int c_right=diameter(root->right,max_dia);
    max_dia=max(max_dia,c_left+c_right+1);
    return max(c_left,c_right)+1;
}
int main(){
  node* root = buildtree();
  /*preorder(root);
  cout<<"\n";
  postorder(root);
  cout<<"\n";
  inorder(root);
  */
  /*int h=height(root);
  cout<<h<<"\n";
  for(int i=0;i<h;i++){
      level(i,root);
      cout<<"\n";
  }
  */
  /*levelorder(root);
  cout<<countnodes(root)<<"\n";
  cout<<sumnodes(root)<<"\n";
  */
  int max_diameter=0;
  diameter(root,max_diameter);
  cout<<max_diameter<<"\n";
    return 0;
}
