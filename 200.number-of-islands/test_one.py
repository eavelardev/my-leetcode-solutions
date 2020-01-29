import time
from number_of_islands_me import *
from data import *

if __name__ == "__main__":
    solution = Solution()

    for i in range(len(inputs)):
        if solution.numIslands(inputs[i]) != outputs[i]:
            print("Fail in test: ", i)
            exit(0)

    num_tests = 10
    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            solution.numIslands(input)

    toc = time.clock()

    print(round((toc-tic) * 1000), "ms with", num_tests, "tests")
