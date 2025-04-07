"""
36. Valid Sudoku
Solved
Medium
Topics
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution(object):
    def ValidSudoku(board):
    # Sets to keep track of numbers seen in rows, columns, and 3x3 sub-grids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_grids = [set() for _ in range(9)]  # 3x3 sub-grid sets
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue  # Skip empty cells
                
                # Check if the number already exists in the current row, column or sub-grid
                if num in rows[i]:  # Check row
                    return False
                if num in cols[j]:  # Check column
                    return False
                sub_grid_index = (i // 3) * 3 + (j // 3)  # Determine which sub-grid we are in
                if num in sub_grids[sub_grid_index]:  # Check sub-grid
                    return False
                
                # Add the number to the corresponding row, column, and sub-grid
                rows[i].add(num)
                cols[j].add(num)
                sub_grids[sub_grid_index].add(num)
        
        return True



# Explanation of how the sub-grid index is calculated:
# 
# The board is divided into nine 3x3 sub-grids, which can be visualized like this:
#
# Sub-grid 0 | Sub-grid 1 | Sub-grid 2
# -------------------------------------
# Sub-grid 3 | Sub-grid 4 | Sub-grid 5
# -------------------------------------
# Sub-grid 6 | Sub-grid 7 | Sub-grid 8
#
# Each sub-grid contains cells from specific rows and columns. 
# For instance:
# - Sub-grid 0 contains cells from rows 0-2 and columns 0-2.
# - Sub-grid 1 contains cells from rows 0-2 and columns 3-5.
# - Sub-grid 2 contains cells from rows 0-2 and columns 6-8.
# - Sub-grid 6 contains cells from rows 6-8 and columns 0-2 (which is the sub-grid of the cell [7][2]).
# 
# For any cell at position [i][j], we calculate which sub-grid it belongs to using this formula:
#
# sub_grid_index = (i // 3) * 3 + (j // 3)
#
# Explanation:
# - i is the row index of the cell.
# - j is the column index of the cell.
# - i // 3 and j // 3 divide the row and column indices by 3 and give the sub-grid's row and column.
# - The formula `(i // 3) * 3 + (j // 3)` computes the unique sub-grid index.
#
# For example, for the cell at position [7][2]:
# - i = 7, j = 2
# - i // 3 = 7 // 3 = 2
# - j // 3 = 2 // 3 = 0
# - sub_grid_index = (2 * 3) + 0 = 6
# This means that the cell [7][2] belongs to sub-grid 6.
#
# Here’s the mapping of sub-grids:
# - Sub-grid 0: Rows 0-2, Columns 0-2
# - Sub-grid 1: Rows 0-2, Columns 3-5
# - Sub-grid 2: Rows 0-2, Columns 6-8
# - Sub-grid 3: Rows 3-5, Columns 0-2
# - Sub-grid 4: Rows 3-5, Columns 3-5
# - Sub-grid 5: Rows 3-5, Columns 6-8
# - Sub-grid 6: Rows 6-8, Columns 0-2
# - Sub-grid 7: Rows 6-8, Columns 3-5
# - Sub-grid 8: Rows 6-8, Columns 6-8
#
# Explanation of `set()` usage:
# - A `set` is a built-in data structure in Python that stores unique elements. 
# - It is used in this solution to track the numbers we have seen in each row, column, and sub-grid.
# - The reason we use a `set` is that it allows us to quickly check if a number has already been added 
#   (using the `in` operator) and also efficiently add new numbers.
# - Sets are ideal for this problem because they automatically handle duplicate values. 
#   If a number is already in the set, we know that it's a duplicate, and we can return `False` immediately.
# 
# Using sets for rows, columns, and sub-grids ensures that we can check for duplicates in O(1) time.
# The space complexity for storing the sets is also O(1), since the number of rows, columns, and sub-grids 
# is constant (9 in each case).
#
# Time complexity:
# - The time complexity of the solution is O(1) because the board size is fixed at 9x9, 
#   and we are iterating through a constant number of cells (81 cells in total).
# - Checking membership and adding items to a set takes constant time on average, so 
#   each iteration of the loop is O(1).

