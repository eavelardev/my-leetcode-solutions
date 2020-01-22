#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
class Solution:
    def shortestBridge(self, A):
        m, n = len(A), len(A[0])
        graph = {}
        
        def neighbors(i,j, comp):
            for k, l in ((i,j-1),(i-1,j),(i,j+1),(i+1,j)):
                if 0 <= k < m and 0 <= l < n and A[k][l] == comp:
                    yield k, l 
                    
        def dfs(node, visited, coast):
            visited[node] = True
            
            for k,l in neighbors(*node, 0):
                coast.add((k,l))
            
            for next_node in graph[node]:
                if visited[next_node] is False:
                    dfs(next_node, visited, coast)
        
        for i in range(m):
            for j in range(n):                
                if A[i][j]:      
                    graph[(i,j)] = [(k,l) for k,l in neighbors(i,j, 1)]

        visited = {node: False for node in graph}
        coasts = []

        for node in graph:
            if visited[node] is False:
                coast = set()
                dfs(node, visited, coast)
                coasts.append(coast)

        coast1, coast2 = coasts
        size_bridge = 1
        
        while True:
            if len(coast1 & coast2):
                return size_bridge

            for i, j in coast1:
                A[i][j] = 1

            new_coast = set()
            for node in coast1:
                for k, l in neighbors(*node, 0):
                    new_coast.add((k,l))

            coast1 = new_coast
            size_bridge += 1
           
# @lc code=end

import time
import sys 
from shortest_bridge_tests import *

sys.setrecursionlimit(10**6) 

if __name__ == "__main__":
    solution = Solution()
    tic = time.clock()
    for f in range(num_tests):
        for h in range(len(inputs)):
            solution.shortestBridge(inputs[h])
    toc = time.clock()

    print(round(toc-tic, 3))

