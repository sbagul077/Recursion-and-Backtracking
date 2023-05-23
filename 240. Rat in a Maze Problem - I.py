class Solution:
    dirs = list()
    visited = list()

    def findPath(self, m, n):
        # code here
        result = list()
        self.visited = [[0] * n for i in range(n)]
        self.dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # right    down      up      left
        # print(self.dirs, self.visited)
        if m[0][0] == 1:
            self.helper(m, n, result, 0, 0, list())
        return result

    def helper(self, m, n, result, row, col, path):
        # if we reach the last index
        # append copy of the path in result array
        if row == n - 1 and col == n - 1:
            result.append("".join(path))
            return

        nav = "RDUL"

        for i in range(len(self.dirs)):

            d = self.dirs[i]
            nr = row + d[0]
            nc = col + d[1]
            if n > nr >= 0 == self.visited[nr][nc] and 0 <= nc < n and m[nr][nc] == 1:
                self.visited[row][col] = 1
                path.append(nav[i])
                self.helper(m, n, result, nr, nc, path)
                path.pop()
                self.visited[row][col] = 0


# Recursion, backtracking
# Time Complexity: O(4 ^(m*n))
# Space Complexity:O(m*n)

n = 4
m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
if __name__ == "__main__":
    obj = Solution()
    print(obj.findPath(m, n))
