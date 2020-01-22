#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start

# from typing import List

class Solution:  
    def spiralOrder(self, matrix):
        spiral_list = []
        i = 0

        while len(matrix) > 0:
            opt = i % 4

            if opt == 0:    # right
                elems = self.get_row(matrix, 0)
            elif opt == 1:  # down
                elems = self.get_col(matrix, -1)
            elif opt == 2:  # left
                elems = self.get_row(matrix, -1)
                elems.reverse()
            elif opt == 3:  # up
                elems = self.get_col(matrix, 0)
                elems.reverse()

            spiral_list.extend(elems)
            i += 1

        return spiral_list

    def get_col(self, matrix, c):
        elems = [row[c] for row in matrix]

        for row in matrix:
            row.pop(c)

        if len(matrix[0]) == 0:
            matrix.clear()

        return elems

    def get_row(self, matrix, r):
        elems = matrix[r]
        matrix.pop(r)

        return elems

# @lc code=end
