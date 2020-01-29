#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start

class Solution:  
    def spiralOrder(self, matrix):

        def get_col(matrix, c):
            elems = [row[c] for row in matrix]

            for row in matrix:
                row.pop(c)

            if len(matrix[0]) == 0:
                matrix.clear()

            return elems

        def get_row(matrix, r):
            elems = matrix[r]
            matrix.pop(r)

            return elems
            
        spiral_list = []
        i = 0

        while len(matrix) > 0:
            opt = i % 4

            if opt == 0:    # right
                elems = get_row(matrix, 0)
            elif opt == 1:  # down
                elems = get_col(matrix, -1)
            elif opt == 2:  # left
                elems = get_row(matrix, -1)
                elems.reverse()
            elif opt == 3:  # up
                elems = get_col(matrix, 0)
                elems.reverse()

            spiral_list.extend(elems)
            i += 1

        return spiral_list

# @lc code=end
