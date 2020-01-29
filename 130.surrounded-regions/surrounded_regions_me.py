#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def dfs(self, graph, node, visited, region):
        visited[node] = True
        region.append(node)

        for next_node in graph[node]: 
            if visited[next_node] is False: 
                self.dfs(graph, next_node, visited, region) 
                
                
    def solve(self, board):
        m = len(board)

        if m < 3: 
            return board

        n = len(board[0])

        if n < 3:
            return board

        pos = [[j+n*i for j in range(n)] for i in range(m)]
        border_nodes = []
        graph = {}

        for i in range(m):
            for j in range(n):                
                if board[i][j] == 'O':
                    adjacent = [(k, l) for k,l in [(i,j-1),(i-1,j),(i,j+1),(i+1,j)] 
                                            if 0 <= k < m and 0 <= l < n]             
                    graph[pos[i][j]] = [pos[k][l] for k,l in adjacent if board[k][l]=='O']

                    if i in [0, m-1] or j in [0, n-1]: # border
                        border_nodes.append(pos[i][j])

        visited = {node: False for node in graph} 
        cells_to_flip = []

        for node in graph:
            if visited[node] is False:
                region = []
                self.dfs(graph, node, visited, region)

                node_border = False
                for node in region:
                    if node in border_nodes:
                        node_border = True
                        break

                if node_border is False:
                    cells_to_flip.extend(region)

        for cell in cells_to_flip:
            i = cell//n
            j = cell-i*n
            board[i][j] = 'X'

        return board

        
# @lc code=end

