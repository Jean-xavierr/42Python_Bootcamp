import copy

# work in progress


class Vector:

    def __init__(self, elem) -> None:
        if not isinstance(elem, (int, tuple, list)):
            print('Error: initialization, only int, tuple or list.')
            return
        if isinstance(elem, int) and elem < 1:
            print('Error: int can\'t be negative.')
            return
        if isinstance(elem, int):
            self.vector = [[float(nb)] for nb in range(elem)]
            self.shape = (elem, 1)
            print(self.vector, self.shape)
        elif isinstance(elem, tuple) and len(elem) == 2:
            self.vector = [[float(nb)] for nb in range(*elem)]
            self.shape = (elem[1] - elem[0], 1)
            print(self.vector, self.shape)
        elif isinstance(elem, list):
            if self.check_shape_1_x(elem):
                self.vector = copy.deepcopy(elem)
                self.shape = (1, len(elem))
                print(self.vector, self.shape)
            elif self.check_shape_x_1(elem):
                self.vector = copy.deepcopy(elem)
                self.shape = (len(elem), 1)
                print(self.vector, self.shape)
        return

    @staticmethod
    def check_shape_1_x(lst: list) -> bool:
        return all([isinstance(elem, float) for elem in lst])

    @staticmethod
    def check_shape_x_1(lst: list) -> bool:
        return all([isinstance(elem, list) and
                    len(elem) == 1 and isinstance(elem[0], float)
                    for elem in lst])

    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector):
            print('Error: instance must be a Vector.')
            return
        if self.shape[0] == 1:
            print('Shape size (1, *)')
        else:
            print('Shape size (*, *)')

    def __radd__(self, other_vector):
        print('radd')

    def __sub__(self, other_vector):
        print('sub')

    def __rsub(self, other_vector):
        print('rsub')

    def __truediv__(self, other_vector):
        print('truediv')

    def __rtruediv__(self, other_vector):
        print('rtruediv')

    def __null__(self):
        print('null')

    def __str__(self) -> str:
        return (f'Vector: {self.vector}')

    def __repr__(self) -> str:
        return (f'{self.vector}')


Vector(3)
Vector((10, 15))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([0.0, 1.0, 2.0, 3.0])
v3 = Vector([1.0, 1.0, 1.0, 1.0])