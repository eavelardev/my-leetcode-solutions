from spiral_matrix_leetcode import *
# from spiral_matrix_my import *
from data import *

if __name__ == "__main__":
    solution = Solution()

    for i in range(len(inputs)):
        if solution.spiralOrder(inputs[i]) != outputs[i]:
            print("Fail in test: ", i)
            exit(0)

    print("OK!")
