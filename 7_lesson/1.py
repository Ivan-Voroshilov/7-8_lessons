
class Matrix:
    matr = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                self.matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return self.matr

    def __str__(self):
        return f'{self.matr[0]}\n{self.matr[1]}\n{self.matr[2]}'


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])


print(my_matrix.__add__())
print(my_matrix.__str__())
