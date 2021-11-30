import sys


if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    else:
        print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")
elif len(sys.argv) == 2 and not sys.argv[1].isnumeric():
    print('Error')
elif len(sys.argv) > 2:
    print('Error')
