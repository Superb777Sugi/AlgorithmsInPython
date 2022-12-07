def solution(num_list: list) -> list:
    """
    >>> solution([1 2 3 4 5])
    [5, 4, 3, 2, 1]
    >>> solution([1, 1, 1, 1, 1, 2])
    [2, 1, 1, 1, 1, 1]
    >>> solution([1, 0, 1, 1, 1, 3, 5])
    [5, 3, 1, 1, 1, 0, 1]
    """
    answer = num_list[::-1]
    return answer
