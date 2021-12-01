import sys


def usage() -> None:
    print("Usage: python filterwords.py <str> <int>\n"
          "Example:\n\tpython filterwords.py \"Hello, my friend\" 3")


def remove_punctuation(str: str) -> str:
    punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    for letter in str:
        if letter in punc:
            str = str.replace(letter, "")
    return str


def filterwords(str: str, n: str) -> list:
    str = remove_punctuation(str)
    filter_list = [word for word in str.split() if len(word) > n]
    return filter_list


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if not sys.argv[2].isnumeric():
            print('Error: the second argument must be a positive number\n')
            usage()
        else:
            print(filterwords(sys.argv[1], int(sys.argv[2])))
    else:
        usage()
