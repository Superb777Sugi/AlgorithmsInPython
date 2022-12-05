def solution2(n: int) -> list:
    """
    >>> solution(10)
    [1, 3, 5, 7, 9]
    >>> solution(10)
    [1, 3, 5, 7, 9, 11, 13, 15]
    """
    return [i for i in range(1, n + 1, 2)]


def solution1(n: int) -> list:
    """
    >>> solution(10)
    [1, 3, 5, 7, 9]
    >>> solution(10)
    [1, 3, 5, 7, 9, 11, 13, 15]
    """
    answer = []
    for i in range(1, n + 1, 2):
        answer.append(i)
    return answer
