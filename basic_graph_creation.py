def addEdge(i,j,graph):
    graph[i].append(j)
    graph[j].append(i)

def printGraph(graph):
    for i in range(1,len(graph)):
        print(i, end=" => ")
        for j in graph[i]:
            print("{}, ".format(j), end="")
        print()

def removeEdge(i,j,graph):
    graph[i].remove(j)
    graph[j].remove(i)
    
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
    
    print(adjMat)
    printGraph(graph)
    
