import sys

# input
origin_alphabet = sys.stdin.readline().strip()

# next alphabet
next_alphabet = chr(ord(origin_alphabet) + 1)

# upper alphabet
upper_alphabet = origin_alphabet.upper()

# output
sys.stdout.write(f"{next_alphabet} {upper_alphabet}")
