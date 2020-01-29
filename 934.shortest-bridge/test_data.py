i# from shortest_bridge_leetcode import *
from shortest_bridge_me import *
from data import *

if __name__ == "__main__":
    solution = Solution()

    for i in range(len(inputs)):
        if solution.shortestBridge(inputs[i]) != outputs[i]:
            print("Fail in test: ", i)
            exit(0)

    print("OK!")
