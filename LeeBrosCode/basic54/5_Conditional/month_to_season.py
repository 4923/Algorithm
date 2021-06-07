import sys

# input (1<=m<=12)
m = int(sys.stdin.readline().strip())

# output
if 3 <= m <= 5:
    sys.stdout.write("봄")
elif 6 <= m <= 8:
    sys.stdout.write("여름")
elif 9 <= m <= 11:
    sys.stdout.write("가을")
elif m == 12 or 1 <= m <= 2:
    sys.stdout.write("겨울")
