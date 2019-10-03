from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self,vertices):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = vertices

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)


        def DFSUtil(self, v, visited):

            # Mark the current node as visited
            # and print it
            visited[v] = True
            print(v, end=' ')

            # Recur for all the vertices
            # adjacent to this vertex
            for i in self.graph[v]:
                if visited[i] == False:
                    self.DFSUtil(i, visited)

                    # The function to do DFS traversal. It uses

        # Call the recursive helper function
        # to print DFS traversal
        DFSUtil(v, visited)
        
    # DFS版本的拓扑排序
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    def topologicalSort_DFS(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print(stack) 
        
        
    def topologicalSort_BFS(self):     
        in_degree = [0] * (self.V)

        # 先进行入度的计算
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
                
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
                
        top_order = []        
        # 计算收否节点数量一致       
        cnt = 0
        while queue:
            u = queue.pop(0)
            top_order.append(u)
            # 找他的下次层，减去1
            for i in self.graph[u]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    queue.append(i)
            cnt += 1
        
        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            # Print topological order
            print(top_order)
            
# Create a graph given
# in the above diagram
# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# g.DFS(2)
# g.BFS(2)

g2 = Graph(6)
g2.addEdge(5, 2);
g2.addEdge(5, 0);
g2.addEdge(4, 0);
g2.addEdge(4, 1);
g2.addEdge(2, 3);
g2.addEdge(3, 1);
# g2.topologicalSort_DFS
g2.topologicalSort_BFS()


"""
# 79. Word Search:BFS
- 题目：找到相邻的字母可以串出单词，相邻指的是正方向的4个

例子：   
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
# 因为找相邻使用BFS
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        
        #找到第一个字母
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 若找到了单词则返回true
                if self.bfs(board, i,j,word):
                    return True
                    

    def bfs(self, board,i,j word):
    #  找连续的值,若长度为0则返回
    if len(word) == 0:
        return True
    if i<0 or j<0 or i>=len(board) or j>=len(board) or word[0] != board[i][j]:
        return False
    # 确保走过排除
    tmp = board[i][j]
    board[i][j] = '#'
    res = self.bfs(self,board,i-1,j word[1,:]) or self.bfs(self,board,i+1,j word[1,:]) or
          self.bfs(self,board,i,j-1 word[1,:]) or self.bfs(self,board,i,j+1 word[1,:])
    board[i][j] = tmp
    return res
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["v","D","E","E"]]

word = "SEE"
s = Solution()
print(s.exist(board, word))
"""
1091. Shortest Path in Binary Matrix:DFS
    题目：从最左上走到最右下的位置，只有为0的点可以走通，为1的不通，8个方向都可以问最少几个点
    input = [[0,0,0],[1,1,0],[1,1,0]]
    output =4
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 将想放的数据用q装进去进行遍历
        if grid[0][0] or grid[n-1][n-1]:
            print('你输入的数据必须首位值为0')
            return -1
        n = len(grid)
        queue = [(0,0,1)]
        for i,j,d in queue:
            # 当到最后的时候返回
            if i == n-1 and j == n-1:return d
            for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),
               (i+1,j),(i+1,j+1)):
                if grid[x][y] == 0 and 0<=x<n and 0<=y<n:
                    # 走过的路就不走了
                    grid[x][y] = 1
                    queue.append((x,y,d+1))
        
inputs = [[0,0,0],[1,1,0],[1,1,0]]        
a = Solution()        
a.shortestPathBinaryMatrix(inputs)