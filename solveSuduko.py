board = [
                ["5", "3", ".", ".", 7, ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", ".", "2", "8"],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board, row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[i][row] == c:
                    return False
                row_index = 3 * (row // 3) + i // 3
                col_index = 3 * (col // 3) + i % 3
                if board[row_index][col_index] == c:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                     for c in range(1, 10):
                           if isValid(board, row, col, chr(c+ord("0"))):
                                return True
                            else:
                                board[row][col] = "."
                return False
        return True

    solve(board)
