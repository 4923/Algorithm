# [Import Module]
import sys  # sys.stdin.readline()

# [Input Data]
# line 1: 1 <= n <= 200, 1 <= t <= 1000
n, t = map(int, sys.stdin.readline().strip().split())
# line 2: Upper belt Numbers (len = n, each elements number range is 1~9)
upp = [
    list(map(int, sys.stdin.readline().strip().split())) 
    for _ in range(n)
]

# line 3 : Lower belt Numbers (len = n, each elements number range is 1~9)
low = [
    list(map(int, sys.stdin.readline().strip().split())) 
    for _ in range(n)
]

# [TURN conveyor]
def turn(before_row, before_col):
    # Largest after coordinate is: n

    temp = 0
    for i in range(2):  # [ROW] two side of conveyor belts
        for j in range(n):  # [COL] numbers on the conveyor belt
            # The moment arrived edge of conveyor belt: multiple -1 at before_col to reverse numeric sign
            if j + 1 == n:
                temp = upp[i][j]
                before_col *= -1

            else:
                temp = upp[i][j] 
                upp[i][j] = upp[i][j+1]
            



    return



# [MAIN]
def main():
    current = turn(0, 0, n, n)  # BaseCase
    for i in range(n):
        turn(

    return


if __name__ == '__main__':
    main()