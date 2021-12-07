from random import sample


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        print("ERROR")
        return []
    lst = text.split(sep)
    if option:
        if option == 'unique':
            lst = set(lst)
        elif option == 'ordered':
            lst.sort()
        elif option == 'shuffle':
            lst = sample(lst, len(lst))
        else:
            print("ERROR")
            return []
    for elem in lst:
        yield elem


if __name__ == '__main__':
    text = "This is a simple string for a basic test. Very simple."
    for word in generator(text, option="shuffle"):
        print(word)
