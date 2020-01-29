import time
import sys
from shortest_bridge_leetcode import *
# from shortest_bridge_my import *
from test_data import *

sys.setrecursionlimit(10**6)

if __name__ == "__main__":
    solution = Solution()

    for i in range(len(inputs)):
        if solution.shortestBridge(inputs[i]) != outputs[i]:
            print("Fail in test: ", i)
            exit(0)

    num_tests = 10
    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            solution.shortestBridge(input)

    toc = time.clock()

    print(round((toc-tic) * 1000), "ms with", num_tests, "tests")
