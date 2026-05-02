class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check all rows
        for row in range(9):
            seen = set()
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in seen:      # ← fixed
                    return False
                seen.add(cell)        # ← fixed (was adding 'col')

        # 2. Check all columns
        for col in range(9):
            seen = set()              # ← reusing the same name "seen" is fine
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # 3. Check all 3×3 boxes
        for box_row in range(3):      # 0, 1, 2
            for box_col in range(3):  # 0, 1, 2
                seen = set()          # ← again, same variable name
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row*3 + i][box_col*3 + j]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)

        return True                   # ← only return True if everything passed