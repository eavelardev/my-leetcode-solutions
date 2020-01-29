import time
import spiral_matrix_leetcode
import spiral_matrix_my
from data import *

if __name__ == "__main__":
    leetcode_solution = spiral_matrix_leetcode.Solution()
    my_solution = spiral_matrix_my.Solution()

    num_tests = 10000
    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            leetcode_solution.spiralOrder(input)

    toc = time.clock()

    print("leetcode_solution:", round((toc-tic) * 1000), "ms with", num_tests, "tests")

    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            my_solution.spiralOrder(input)

    toc = time.clock()

    print("my_solution:", round((toc-tic) * 1000), "ms with", num_tests, "tests")
