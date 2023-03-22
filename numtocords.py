def num_to_coords(num):
    row = (num - 1) // 3
    col = (num - 1) % 3
    return (row, col)
