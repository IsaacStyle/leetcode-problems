def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == '.':
                    continue
                elif (curr in rows[r] or
                    curr in cols[c] or
                    curr in sqrs[r // 3, c // 3]):
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                sqrs[r // 3, c // 3].add(curr)

        return True