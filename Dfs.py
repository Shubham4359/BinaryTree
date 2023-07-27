def dfs(n,graph,vis):
    global cnt
    vis[n]=1
    #print(n," ")
    leaf=True
    for i in graph[n]:
        if vis[i]==0:
            leaf=False
            dfs(i,graph,vis)
    if leaf:
        cnt=cnt+1
            
def bfs(graph,src,des):
    # Create a queue for BFS
    queue = []
    dis = [0]*(n+1)
    par = [0]*(n+1)
    vis = [0]*(n+1) 
    # Add the source node in
    # visited and enqueue it
    queue.append(src)
    vis[src]=1
    par[src]=-1
    dis[src]=0
 
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        #print (s, end = " ")
 
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then add it
        # in visited and enqueue it
        for i in graph[s]:
            if vis[i]==0:
                queue.append(i)
                vis[i]=1
                dis[i]=dis[s]+1 
                par[i]=s
                
    
if __name__ == '__main__':
     
    #  n is the number of vertices
    #  m is the number of edges
    graph = []
    n, m = map(int, input().split())
    for i in range(n+1):
        graph.append([])
    adjMat = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        adjMat[u][v] = 1
        adjMat[v][u] = 1
        graph[v].append(u)
        graph[u].append(v)
        # for a directed graph with an edge
        # pointing from u to v,we just assign
        # adjMat[u][v] as 1
    cnt=0
    #print(adjMat)
    vis = [0]*(n+1)
    bfs(graph,1,n)
    dfs(1,graph,vis)
    print(cnt)
    
