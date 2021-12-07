class GotCharacter:
    """A class for create Got Character."""
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family.
    \rOr when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print("Winter is COming")

    def die(self):
        self.is_alive = False


if __name__ == '__main__':
    arya = Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    print(arya.__doc__)
    # ------
    print()
    any_value = GotCharacter()
    print(any_value.__dict__)
    # ------
    print()
    luigi = GotCharacter('Luigi', True)
    print(luigi.__doc__)
