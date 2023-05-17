def isValidSudoku(self, board):
        for i in range(len(board)):
            row_map = {}
            col_map = {}
            for j in range(len(board[i])):
                curr = board[i][j]
                curr_col = board[j][i]
                if curr != '.' and curr in row_map:
                    return False
                if curr_col != '.' and curr_col in col_map:
                    return False
                col_map[curr_col] = col_map.get(curr_col,0)
                row_map[curr] = row_map.get(curr,0)
        return True