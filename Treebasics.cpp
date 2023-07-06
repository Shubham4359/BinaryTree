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
    if(root->left!=NULL){level(cur-1,root->left);}
    if(root->right!=NULL){level(cur-1,root->right);}
}
int main(){
  node* root = buildtree();
  /*preorder(root);
  cout<<"\n";
  postorder(root);
  cout<<"\n";
  inorder(root);
  */
  int h=height(root);
  cout<<h<<"\n";
  for(int i=0;i<h;i++){
      level(i,root);
      cout<<"\n";
  }
    return 0;
}



