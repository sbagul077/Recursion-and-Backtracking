# User function Template for python3


# Function to determine if graph can be coloured with at most M colours such
# that no two adjacent vertices of graph are coloured with same colour.

def isSafe(node, color, graph, n, col):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


def solve(node, color, m, N, graph):
    if node == N:
        return True

    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0

    return False


def graphColoring(graph, m, N):
    # your code here
    color = [0] * N
    if solve(0, color, m, N, graph):
        return 1
    return 0


# Graph, Recursion
# Time Complexity: O(n^m)
# Space Complexity: O(h). Height of the recursion stack
# {
# Driver Code Starts
# Initial Template for Python 3
V = 5
k = 4
m = 3
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
if __name__ == "__main__":
    # t = int(input())
    # while (t > 0):
    # V = int(input())
    # k = int(input())
    # m = int(input())
    # list = [int(x) for x in input().strip().split()]
    # graph = [[0 for i in range(V)] for j in range(V)]
    # cnt = 0
    # for i in range(m):
    #     graph[list[cnt] - 1][list[cnt + 1] - 1] = 1
    #     graph[list[cnt + 1] - 1][list[cnt] - 1] = 1
    #     cnt += 2
    if graphColoring(graph, k, V):
        print(1)
    else:
        print(0)

    # t = t - 1

# } Driver Code Ends
