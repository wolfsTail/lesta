"""
Алгоритм сортирвоки массива целых чисел
"""

def get_pivot(array: list[int], start: int, end: int) -> int:
    """
    args:
        array (list): Массив целых чисел
        start (int): Начальная позиция
        end (int): Конечная позиция
    return:
        int: Медиана
    """
    mid = (start + end) // 2    
    if (array[start] <= array[mid] and array[mid] <= array[end]) or\
        (array[end] <= array[mid] and array[mid] <= array[start]):
        return array[mid]
    if (array[mid] <= array[start] and array[start] <= array[end]) or\
        (array[end] <= array[start] and array[start] <= array[mid]):
        return array[start]
    return array[end]

def quicksort(array: list[int]) -> list[int]:
    """
    args:
        A (list): Массив целых чисел
        start (int): Начальная позиция
        end (int): Конечная позиция
    return:
        list: отсоортированный массив целыйх чисел
    """
    if len(array) < 2:
        return array
    
    pivot = get_pivot(array, 0, len(array) - 1)

    low = [digit for digit in array if digit < pivot]
    more = [digit for digit in array if digit > pivot]
    equal = [digit for digit in array if digit == pivot]

    return quicksort(low) + equal + quicksort(more)
