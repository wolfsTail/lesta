"""
Алгоритмы определения четности целого числа.
"""

def isEven(value):
    """
    Arg:
        value (int): Целое число для проверки.
    Return:
        bool: True, если число четное, иначе False.
    """
    return value % 2 == 0

def is_even(value: int) -> bool:
    """
    Arg:
        value (int): Целое число для проверки.
    Return:
        bool: True, если число четное, иначе False.
    """
    return bool(int(bin(value)[-1]))
