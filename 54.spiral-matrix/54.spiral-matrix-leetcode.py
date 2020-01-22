#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

# @lc code=end

import time
from spiral_matrix_tests import *

if __name__ == "__main__":
    tic = time.clock()
    for _ in range(num_tests):
        for j in range(len(inputs)):
            solution = Solution()
            solution.spiralOrder(inputs[j])
    toc = time.clock()

    print(round(toc-tic, 3))
