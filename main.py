# create a 3x3 grid

row0: list = [-1] * 3
row1: list = [-1] * 3
row2: list = [-1] * 3

grid: list = [row0, row1, row2]

# Find shape by parameters: row and col
def FindShape(row: int, col: int) -> int:
    # Retrieve the row
    row_: list = grid[row]
    # Retrieve the shape
    shape: int = row_[col]
    return shape

shape = FindShape(0,2)
print(shape)
