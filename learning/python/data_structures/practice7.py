from abc import ABC, abstractmethod
import math

"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — 
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

# class Matrix:
#     def __init__(self, *matrix: list):
#         self.matrix = list(matrix)
#
#     def __str__(self):
#         matrix_converted_to_string_format = ''
#         for matrix_string in self.matrix:
#             for matrix_element in matrix_string:
#                 matrix_converted_to_string_format += f'{matrix_element} '
#             matrix_converted_to_string_format += '\n'
#         return matrix_converted_to_string_format
#
#     def __add__(self, other):
#         i = 0
#         j = 0
#         added_matrix = []
#         for i in range(len(self.matrix)):
#             added_matrix_string = []
#             for j in range(len(self.matrix)):
#                 added_matrix_string.append(self.matrix[i][j] + other.matrix[i][j])
#             added_matrix.append(added_matrix_string)
#         return Matrix(added_matrix)
#
#
# matrix_1 = Matrix([1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 0], [6, 6, 8, 9, 10, 55])
# # matrix_1 = [[1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 0], [6, 6, 8, 9, 10, 55]]
# matrix_2 = Matrix([1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 0], [6, 6, 8, 9, 10, 55])
# matrix_3 = matrix_1 + matrix_2
# print(matrix_3)
## Почему то не складывает остальные элементы матрицы. Дело в том, что в строке 40 надо задать длинну списка строки
## а он не даёт задать лен(селф.матрикс_стринг) в адд =(

"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта 
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, 
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

# class Clothes:
#     def __init__(self, type_of_clothes: str):
#         self.type_of_clothes = type_of_clothes
#
#     def __str__(self):
#         return f'Одежда типа: {self.type_of_clothes}'
#
#
# class Coat(Clothes):
#     def __init__(self, type_of_clothes, size_V):
#         super().__init__(type_of_clothes)
#         self.size_V = size_V
#
#     @abstractmethod
#     def fabric_consumption(self):
#         return self.size_V / 6.5 + 0.5
#
#     def __add__(self, other):
#         return self.fabric_consumption() + other.fabric_consumption()
#
#
# class Suit(Clothes):
#     def __init__(self, type_of_clothes, size_H):
#         super().__init__(type_of_clothes)
#         self.size_H = size_H
#
#     ## @property
#     @abstractmethod
#     def fabric_consumption(self):
#         return 2 * self.size_H + 0.3
#
#     def __add__(self, other):
#         return self.fabric_consumption() + other.fabric_consumption()
#
#
# clothes_1 = Coat("Пальто 1", 2)
# clothes_2 = Suit("Костюм 1", 2)
# print(clothes_1)
# print(clothes_2)
# print(f'Расход ткани на {clothes_1.type_of_clothes} составляет: {clothes_1.fabric_consumption()}')
# print(f'Расход ткани на {clothes_2.type_of_clothes} составляет: {clothes_2.fabric_consumption()}')
# clotehs_3 = clothes_1 + clothes_2
# print(clotehs_3)
# print(clothes_1.fabric_consumption())


"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки 
(целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к 
клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, 
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше 
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих 
двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() 
вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


# class OrganicCell:
#     def __init__(self, cell_number: str, cells_count: int):
#         self.cells_count = cells_count
#         self.cell_number = cell_number
#
#     def __str__(self):
#         return f'Номер клетки: {self.cell_number}, ячеек в клетке: {self.cells_count}'
#
#     def __add__(self, other):
#         general_cell = self.cells_count + other.cells_count
#         general_cell_number = self.cell_number + other.cell_number
#         return OrganicCell(general_cell_number, general_cell)
#
#     def __sub__(self, other):
#         if (self.cells_count - other.cells_count) > 0:
#             general_cell = self.cells_count - other.cells_count
#             general_cell_number = self.cell_number + other.cell_number
#             return OrganicCell(general_cell_number, general_cell)
#         else:
#             return print('Отрицательный результат!\nПроверьте значение количества ячеек одной из клеток!')
#
#     def __mul__(self, other):
#         general_cell = self.cells_count * other.cells_count
#         general_cell_number = self.cell_number + other.cell_number
#         return OrganicCell(general_cell_number, general_cell)
#
#     def __truediv__(self, other):
#         general_cell = self.cells_count // other.cells_count
#         general_cell_number = self.cell_number + other.cell_number
#         return OrganicCell(general_cell_number, general_cell)
#
#     def make_order(self, cells_in_order: int):
#         ordered_cell = ''
#         one_string = self.cells_count // cells_in_order
#         cuted_string = self.cells_count % cells_in_order
#         i = 0
#         while i != one_string:
#             ordered_cell += '*' * cells_in_order
#             ordered_cell += '\n'
#             i += 1
#         ordered_cell += '*' * cuted_string
#         return ordered_cell
#
#
# organic_cell_1 = OrganicCell('Клетка 1', 6)
# organic_cell_2 = OrganicCell('Клетка 2', 6)
# print(organic_cell_1)
# print(organic_cell_2)
# print(organic_cell_1 + organic_cell_2)
# print(organic_cell_1 * organic_cell_2)
# print(organic_cell_1 / organic_cell_2)
# organic_cell_3 = organic_cell_1 + organic_cell_2
# print(organic_cell_3.make_order(5))
