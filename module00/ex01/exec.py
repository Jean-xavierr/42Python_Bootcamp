import sys


if len(sys.argv) >= 2:
    print(" ".join(sys.argv[1:])[::-1].swapcase())
