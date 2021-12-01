import sys


def is_integer(nb: str) -> bool:
    if nb.isdigit() or nb.startswith('-') and nb[1:].isdigit():
        return True
    return False


def usage() -> None:
    print(f"""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")


def print_operations(sum, difference, product, quotient, remainder) -> None:
    print(f"""Sum:        {sum}
Difference: {difference}
Product:    {product}
Quotient:   {quotient}
Remainder:  {remainder}""")


def operations(nb_one: int, nb_two: int) -> str:
    sum: int = nb_one + nb_two
    difference: int = nb_one - nb_two
    product: int = nb_one * nb_two
    if nb_two == 0:
        quotient = "Error (div by zero)"
        modulo = "Error (modulo by zero)"
    else:
        quotient: int = nb_one / nb_two
        modulo: int = nb_one % nb_two
    print_operations(sum, difference, product, quotient, modulo)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) == 3:
        if not is_integer(sys.argv[1]) or not is_integer(sys.argv[2]):
            print("InputError: only numbers\n")
            usage()
        else:
            operations(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 2:
        print("InputError: not enough arguments\n")
        usage()
    else:
        print("InputError: too many arguments\n")
        usage()
