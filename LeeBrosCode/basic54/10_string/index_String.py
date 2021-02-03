import sys

string = sys.stdin.readline().strip()
partial = sys.stdin.readline().strip()

if partial in string:
    print(string.index(partial))
else:
    print(-1)