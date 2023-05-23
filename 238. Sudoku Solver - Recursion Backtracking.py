from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.helper(board)

    def helper(self, board: list[list[str]]) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for num in "123456789":
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.helper(board) == True:
                                return True
                            else:
                                board[i][j] = "."
                    return False

        return True

    def isValid(self, board: list[list[str]], row: int, col: int, num: str) -> bool:
        for i in range(0, 9):
            if board[row][i] == num:
                return False

            if board[i][col] == num:
                return False

            if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == num:
                return False

        return True


# Recursion backtracking
# Time Complexity: O(9^(n^2)) in the worst case, for each cell in the n2 board, we have 9 possible numbers.
# Space Complexity: O(1)

board = board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

if __name__ == "__main__":
    obj = Solution()
    print(obj.solveSudoku(board))
