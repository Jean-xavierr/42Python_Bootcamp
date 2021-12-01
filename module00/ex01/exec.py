import sys


if len(sys.argv) >= 2:
    argv = list(sys.argv)
    while '' in argv:
        argv.remove('')
    print(" ".join(argv[1:])[::-1].swapcase())
