import sys


morse_code = {
              'A': '.-', 'B': '-...', 'C': '-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----',
              '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----',
              ' ': '/',
}


def morse_encryption(*argv) -> None:
    str_encrypt = []
    for word in argv:
        word = ' '.join(word)
        word = word.upper()
        for letter in word:
            if letter in morse_code.keys():
                str_encrypt.append(morse_code[letter])
            else:
                print("Error")
                return
    print(' '.join(str_encrypt))


if len(sys.argv) > 1:
    morse_encryption(sys.argv[1:])
