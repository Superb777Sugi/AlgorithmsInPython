def solution(numbers: list) -> list:
    """
    >>> solution([1 2 3 4 5])
    [2, 4, 6, 8, 10]
    >>> solution([1, 2, 100, -99, 1, 2, 3])
    [2, 4, 200, -198, 2, 4, 6]
    """
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer
