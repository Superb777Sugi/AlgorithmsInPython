def solution(array: list) -> list:
    """
    >>> solution([1, 2, 7, 10, 11])
    7
    >>> solution([9, -1, 0])
    0
    """
    answer = 0
    array.sort()
    length = len(list(array))
    if (length % 2) != 0:
        answer = array[length // 2]
    else:
        answer = None
    return answer
