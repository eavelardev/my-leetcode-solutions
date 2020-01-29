import time
from spiral_matrix_leetcode_simulation import *
# from spiral_matrix_leetcode_layer_by_layer import *
# from spiral_matrix_my import *
from data import *

if __name__ == "__main__":
    solution = Solution()

    num_tests = 100000
    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            solution.spiralOrder(input)

    toc = time.clock()

    print(round((toc-tic) * 1000), "ms with", num_tests, "tests")
