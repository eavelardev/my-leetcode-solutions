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

import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self): self.assertEqual(self.solution.spiralOrder(self.inputs[0]), self.outputs[0])
    def test2(self): self.assertEqual(self.solution.spiralOrder(self.inputs[1]), self.outputs[1])
    def test3(self): self.assertEqual(self.solution.spiralOrder(self.inputs[2]), self.outputs[2])
    def test4(self): self.assertEqual(self.solution.spiralOrder(self.inputs[3]), self.outputs[3])
    def test5(self): self.assertEqual(self.solution.spiralOrder(self.inputs[4]), self.outputs[4])
    def test6(self): self.assertEqual(self.solution.spiralOrder(self.inputs[5]), self.outputs[5])
    def test7(self): self.assertEqual(self.solution.spiralOrder(self.inputs[6]), self.outputs[6])
    def test8(self): self.assertEqual(self.solution.spiralOrder(self.inputs[7]), self.outputs[7])
    def test9(self): self.assertEqual(self.solution.spiralOrder(self.inputs[8]), self.outputs[8])
    def test10(self): self.assertEqual(self.solution.spiralOrder(self.inputs[9]), self.outputs[9])
    def test11(self): self.assertEqual(self.solution.spiralOrder(self.inputs[10]), self.outputs[10])
    def test12(self): self.assertEqual(self.solution.spiralOrder(self.inputs[11]), self.outputs[11])
    def test13(self): self.assertEqual(self.solution.spiralOrder(self.inputs[12]), self.outputs[12])
    def test14(self): self.assertEqual(self.solution.spiralOrder(self.inputs[13]), self.outputs[13])
    def test15(self): self.assertEqual(self.solution.spiralOrder(self.inputs[14]), self.outputs[14])
    def test16(self): self.assertEqual(self.solution.spiralOrder(self.inputs[15]), self.outputs[15])
    def test17(self): self.assertEqual(self.solution.spiralOrder(self.inputs[16]), self.outputs[16])
    def test18(self): self.assertEqual(self.solution.spiralOrder(self.inputs[17]), self.outputs[17])
    def test19(self): self.assertEqual(self.solution.spiralOrder(self.inputs[18]), self.outputs[18])
    def test20(self): self.assertEqual(self.solution.spiralOrder(self.inputs[19]), self.outputs[19])
    def test21(self): self.assertEqual(self.solution.spiralOrder(self.inputs[20]), self.outputs[20])
    def test22(self): self.assertEqual(self.solution.spiralOrder(self.inputs[21]), self.outputs[21])


    inputs = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [],
        [[1]],
        [[2,3]],
        [[3],[2]],
        [[6,9,7]],
        [[7],[9],[6]],
        [[1,2],[3,4]],
        [[2,5],[8,4],[0,-1]],
        [[2,5,8],[4,0,-1]],
        [[1,2,3,4,5,6,7,8,9,10]],
        [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
        [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
        [[2,3,4],[5,6,7],[8,9,10],[11,12,13]],
        [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],
        [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]],
        [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]],
        [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]],
        [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]]
    ]

    outputs = [
        [1,2,3,6,9,8,7,4,5],
        [1,2,3,4,8,12,11,10,9,5,6,7],
        [],
        [1],
        [2,3],
        [3,2],
        [6,9,7],
        [7,9,6],
        [1,2,4,3],
        [2,5,4,-1,0,8],
        [2,5,8,-1,0,4],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10],
        [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13],
        [2,3,4,7,10,13,12,11,8,5,6,9],
        [2,3,4,7,10,13,16,15,14,11,8,5,6,9,12],
        [1,2,3,4,8,12,16,20,19,18,17,13,9,5,6,7,11,15,14,10],
        [1,2,3,4,5,6,12,18,24,30,29,28,27,26,25,19,13,7,8,9,10,11,17,23,22,21,20,14,15,16],
        [1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11],
        [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2],
        [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44,45,46,56,55]
    ]

if __name__ == "__main__":
        unittest.main()
