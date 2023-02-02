from typing import List


class Solution:

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookRow = -1
        rookCol = -1
        for rowInd, row in enumerate(board):
            for colInd, col in enumerate(row):
                if col == 'R':
                    rookRow = rowInd
                    rookCol = colInd
                    break

        pawnsToCapture = 0
        for upRow in range(rookRow-1, -1, -1):
            if board[upRow][rookCol] == 'p':
                pawnsToCapture = pawnsToCapture+1
                #print(str(upRow)+' '+str(rookCol))
                break
            elif board[upRow][rookCol] == 'B':
                break

        for downRow in range(rookRow+1, 8):
            if board[downRow][rookCol] == 'p':
                pawnsToCapture = pawnsToCapture+1
                #print(str(downRow) + ' ' + str(rookCol))
                break
            elif board[downRow][rookCol] == 'B':
                break

        for upCol in range(rookCol-1, -1, -1):
            if board[rookRow][upCol] == 'p':
                pawnsToCapture = pawnsToCapture+1
                #print(str(rookRow) + ' ' + str(upCol))
                break
            elif board[rookRow][upCol] == 'B':
                break

        for downCol in range(rookCol+1, 8):
            if board[rookRow][downCol] == 'p':
                pawnsToCapture = pawnsToCapture+1
                #print(str(rookRow) + ' ' + str(downCol))
                break
            elif board[rookRow][downCol] == 'B':
                break

        return pawnsToCapture


sol = Solution()

print(sol.numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".","p","p","p","p","p",".","."],
    [".","p","p","B","p","p",".","."],
    [".","p","B","R","B","p",".","."],
    [".","p","p","B","p","p",".","."],
    [".","p","p","p","p","p",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]])) #0

print(sol.numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]])) #3

print(sol.numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    ["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."]])) #3

print(sol.numRookCaptures([
    [".",".",".",".",".",".","p","."],
    ["p",".",".",".",".",".","R","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","p","."]])) #3