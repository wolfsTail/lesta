## Алгоритм сортирвоки массива целых чисел

### Реализация

В качестве реализации алгоритма предлагается использовать алгоритм сортировки, предложенный Тони Хоаром. Данный алгоритм явялется наиболее быстрым способом (в среднем $O(n \log n)$), используемым для решения задач соритровки, основанных на сравнении элементов.
Предлагаемый выбор опорного элемента, поможет минимизировать случаи возникновения прогнозируемо "плохих" сценариев входных данных (отсортированный список).

```python

def get_pivot(array: list[int], start: int, end: int) -> int:
    mid = (start + end) // 2    
    if (array[start] <= array[mid] and array[mid] <= array[end]) or\
        (array[end] <= array[mid] and array[mid] <= array[start]):
        return array[mid]
    if (array[mid] <= array[start] and array[start] <= array[end]) or\
        (array[end] <= array[start] and array[start] <= array[mid]):
        return array[start]
    return array[end]

def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array
    
    pivot = get_pivot(array, 0, len(array) - 1)

    low = [digit for digit in array if digit < pivot]
    more = [digit for digit in array if digit > pivot]
    equal = [digit for digit in array if digit == pivot]

    return quicksort(low) + equal + quicksort(more)

```
