import time
import sys
import shortest_bridge_leetcode
import shortest_bridge_me
from data import *

sys.setrecursionlimit(10**4)

if __name__ == "__main__":
    leetcode_solution = shortest_bridge_leetcode.Solution()
    my_solution = shortest_bridge_me.Solution()

    for i in range(len(inputs)):
        if leetcode_solution.shortestBridge(inputs[i]) != outputs[i]:
            print("Fail leetcode_solution in test: ", i)
            exit(0)

        if my_solution.shortestBridge(inputs[i]) != outputs[i]:
            print("Fail my_solution in test: ", i)
            exit(0)

    num_tests = 30
    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            leetcode_solution.shortestBridge(input)

    toc = time.clock()

    print("leetcode_solution:", round((toc-tic) * 1000), "ms with", num_tests, "tests")

    tic = time.clock()
    
    for _ in range(num_tests):
        for input in inputs:
            my_solution.shortestBridge(input)

    toc = time.clock()

    print("my_solution:", round((toc-tic) * 1000), "ms with", num_tests, "tests")
