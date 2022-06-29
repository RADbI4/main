"""
Продлжение рекусрсии.
Задача генерации всех перестановок.
n- чисел от 1 до n- числа которые требуется переставлять.
Перестановок n числе существует n*(n-1)*...*2*1 = n! (n-факториал)
Как выдать эти самые перстановки?! Как сгененрировать?
При помощи рекусрии.

Сгенерируем n возможные чисел в системе счисления n..10
Генерируем от 000...0 до числа n-1...n-1 Длиной М

М-Длина числа
N- основание исчисления
Префикс- обощаем задачу, начинающейся с ничего (None)
Большую задачу генераци сокращается длинна оставшейся части, которую нужно генерировать.
Сгенерировать пвсе перестановки которые начинаются префиксом, с добавлением этой цифры:
"""


def gen_number(
        N: int,
        M: int,
        prefix=None
):
    '''
    Генерирут все числа (с лидирующими незначащими нулями
    в N-ричной системе счисления (N<=10) длины М.
    :param N: основание исчисления
    :param M: Длина числа
    :param prefix:
    :return:
    '''
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    # Без доп. расхода памяти
    # Рекурентный случай:
    for digit in range(N):
        prefix.append(digit)
        gen_number(N, M - 1, prefix)  # задача упрощается за счёт уменьшения количества цифр
        prefix.pop()


def find_in(number, A):
    """
    Ищет number в A и возвращает True, если такой есть и наоборот

    :param number:
    :param A: списк, где нужно найти number
    :return:
    """
    for X in A:
        if number == X:
            return True
    return False


def gen_permutations(N: int, M: int = -1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, начиная с префикса prefix
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    M = N if M == -1 else M  # по умолчанию N чиселв N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep='')
        return
    for number in range(1, N + 1):
        if find_in(number, prefix):
            continue
        prefix.append(number)
        gen_permutations(N, M - 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    gen_permutations(3)
    # gen_number(3, 3) # для произвольной СC
