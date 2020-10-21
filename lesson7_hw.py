# 1
class Matrix:
    def __init__(self, lsvecs):
        self.lsvecs = lsvecs


    def __str__(self):
        return '\n'.join([' '.join([str(ind) for ind in index]) for index in self.lsvecs])

    def __add__(self, other):
        # take dimensions of matrix
        m = len(self.lsvecs)
        n = len(self.lsvecs[0])
        finmat = [[i]*n for i in range(0, m)]  # final matrix
        for ind in range(len(self.lsvecs)):
            for index in range(len(other.lsvecs[ind])):
                finmat[ind][index] = self.lsvecs[ind][index] + other.lsvecs[ind][index]

        return '\n'.join([' '.join([str(ind) for ind in index]) for index in finmat])






mat1 = Matrix([[1, 2, 3], [1, 2, 3], [0, 1, 2]])
mat2 = Matrix([[0, 0, 0], [1, 1, 1], [2, 2, 3]])

print(mat1 + mat2)

# 2
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def tissue_req(self):
        pass

class Coat(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
    @property
    def tissue_req(self):
        return self.width / 6.5 + 0.5

class Jacket(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
    @property
    def tissue_req(self):
        return 2*self.height + 0.3

my_coat = Coat(2, 2)
my_jacket = Jacket(3, 7)
print(f'{my_coat.tissue_req:.2f}')
print(f'{my_jacket.tissue_req:.2f}')
print(f'Общий расход: {(my_coat.tissue_req + my_jacket.tissue_req):.2f}')

# 3

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('операция не выполняется')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, row_cells):
        row = ''
        for i in range(int(self.quantity/row_cells)):
            row += f' {"*" * row_cells} \\n'
        row += f'{"*" * (self.quantity % row_cells)}'
        return row

cell_1 = Cell(25)
cell_2 = Cell(11)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 / cell_2)
print(cell_2.make_order(3))
print(cell_1.make_order(8))


