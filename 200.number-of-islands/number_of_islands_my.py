#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:                
    def numIslands(self, grid):

        def dfs(graph, node, visited):
            visited[node] = True

            for next_node in graph[node]:
                if visited[next_node] is False:
                    dfs(graph, next_node, visited)  

        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])
        pos = [[j+n*i for j in range(n)] for i in range(m)]
        graph = {}

        for i in range(m):
            for j in range(n):                
                if grid[i][j] == '1':
                    adjacent = [(k, l) for k,l in [(i,j-1),(i-1,j),(i,j+1),(i+1,j)]
                                            if 0 <= k < m and 0 <= l < n]            
                    graph[pos[i][j]] = [pos[k][l] for k,l in adjacent if grid[k][l]=='1']

        visited = {node: False for node in graph}
        num_islands = 0

        for node in graph:
            if visited[node] is False:
                dfs(graph, node, visited)
                num_islands += 1

        return num_islands

# @lc code=end
