import sys


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
    difference: int = nb_one - nb_two if nb_one > nb_two else nb_two - nb_one
    product: int = nb_one * nb_two
    if nb_two == 0:
        quotient = "Error (div by zero)"
        modulo = "Error (modulo by zero)"
    else:
        quotient: int = nb_one / nb_two if nb_one > nb_two else nb_two / nb_one
        modulo: int = nb_one % nb_two if nb_one > nb_two else nb_two % nb_one
    print_operations(sum, difference, product, quotient, modulo)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) == 3:
        if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
            print("InputError: only numbers\n")
            usage()
        else:
            operations(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("InputError: too many arguments\n")
        usage()
