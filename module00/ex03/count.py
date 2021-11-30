import string


def text_analyzer(sentences: str = "", *argv) -> None:
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""

    count_character: int = 0
    count_uppercase: int = 0
    count_lowercase: int = 0
    count_punctuation_marks: int = 0
    count_space: int = 0

    if not sentences:
        sentences = input("What is the text to analyse?\n")
    elif len(argv) > 0:
        print("Error")
        return
    for letter in sentences:
        if letter.isdecimal():
            pass
        elif letter.isupper():
            count_uppercase += 1
        elif letter.islower():
            count_lowercase += 1
        elif letter in string.punctuation:
            count_punctuation_marks += 1
        elif letter.isspace():
            count_space += 1
        count_character += 1

    print(f"""The text containts {count_character} characters:
- {count_uppercase} upper letters
- {count_lowercase} lower letters
- {count_punctuation_marks} punctuation marks
- {count_space} spaces""")


if __name__ == "__main__":
    text_analyzer("""Python 2.0, released 2000, introduced
features like List comprehensions and a garbage collection
system capable of collecting reference cycles.""")
