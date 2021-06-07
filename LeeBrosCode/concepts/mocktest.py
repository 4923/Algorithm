import sys

# [input]
# grid_size = n
# block_size = m
# pos_fall = k
grid_size, block_size, pos_fall = map(int, sys.stdin.readline().strip().split())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(grid_size)]

# # input check
# print(f'[INPUT CHECK]\
#     \n\tgrid size: {grid_size}\
#     \n\tblock_size: {block_size}\
#     \n\tpos_fall: {pos_fall}\
#     \n\tgrid: {grid}\n')


def print_grid(grid, grid_size):
    for row in range(grid_size):
        for col in range(grid_size):
            print(grid[row][col], end=" ")
        print()


def possible(grid, grid_size, block_size, pos_fall):
    lowest = 0  # change it when other val is larger

    for max in range(pos_fall - 1, block_size):
        for row in range(grid_size):
            # print(f'[Loop Check]\n\tmax: {max}\n\trow: {row}')

            if grid[row][max] != 0:
                # print(f'\n\t\t\tROW: {row}')
                # print(f'[ROW] {row}')
                # print_grid(fall(grid, grid_size, block_size, pos_fall, lowest), grid_size)
                # print()

                # change
                if row > lowest + 1:  # " lowest + 1"
                    print(f"[Change lowest] row {row} >= lowest {lowest}")
                    lowest = row
                    # print_grid(fall(grid, grid_size, block_size, pos_fall, lowest), grid_size)
                    print()

                # else:
                # print(row, lowest)
                # lowest -= 1
                # print_grid(fall(grid, grid_size, block_size, pos_fall, lowest), grid_size)
                # print()
                # print()

            else:
                # print_grid(fall(grid, grid_size, block_size, pos_fall, lowest), grid_size)
                continue
    # print(f'[lowest] {lowest}')
    return lowest  # int type


def fall(grid, grid_size, block_size, pos_fall, lowest):
    # lowest will be row position of falling block
    grid[lowest]  # line

    for i in range(pos_fall - 1, pos_fall + block_size - 1):
        grid[lowest][i] = "X"
        print(grid)
    return grid  # 2dim Array


def main():

    # -----------------------------
    # # fall func check
    # print('[Fall check]')
    # fall(grid, grid_size, block_size, pos_fall)
    # print('\n')

    # # print func check
    # print('[PRINT GRID]')
    # print_grid(grid, grid_size)
    # print('\n')
    # -----------------------------

    lowest = possible(grid, grid_size, block_size, pos_fall)  # => main
    result = fall(grid, grid_size, block_size, pos_fall, lowest)
    print_grid(result, grid_size)


if __name__ == "__main__":
    main()
