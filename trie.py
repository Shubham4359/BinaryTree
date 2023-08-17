class TRIE:
    def __init__(self, n) -> None:
        self.alph =26
        self.maxn=100000
        self.trie=[[-1]*self.alph]*self.maxn
        self.max_depth=0
        self.nc=0
        self.hot_nodes=[1]*maxn
    
    def insert(self, s):
        cur=0
        for i in range(len(s)):
            c=ord(s[i])-ord('a')
            if self.trie[cur][c] == -1:
                self.nc+=1
                self.trie[cur][c]=self.nc
            cur=self.trie[cur][c]
        self.hot_nodes[cur]+=1

    def exact_check(self, x):
        cur=0
        for i in range(len(x)):
            c=ord(s[i])-ord('a')
            if self.trie[cur][c] == -1:
                return False
            cur=self.trie[cur][c]
        if self.hot_nodes[cur] >0 :
            return True
        else:
            return False
    
    def prefix_check(self, x):
        cur=0
        for i in range(len(x)):
            c=ord(s[i])-ord('a')
            if self.trie[cur][c] == -1:
                return False
            cur=self.trie[cur][c]
        return True
