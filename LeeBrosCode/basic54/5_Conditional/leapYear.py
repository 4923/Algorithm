import sys


def is_leap(y):
    # 4의 배수: leap
    if y // 4 > 0 and y % 4 == 0:
        result = "true"
        # 4의 배수이면서 100의 배수: not leap
        if y // 100 > 0 and y % 100 == 0:
            result = "false"
            # 4의 배수이면서 100의 배수지만 400의 배수: leap
            if y // 400 > 0 and y % 400 == 0:
                result = "true"
            else:
                result = "false"
        else:
            result = "true"
    else:
        result = "false"

    return sys.stdout.write(str(result))


def main():

    # input: 1 <= y <= 2021
    y = int(sys.stdin.readline().strip())

    # output
    is_leap(y)


if __name__ == "__main__":
    main()
