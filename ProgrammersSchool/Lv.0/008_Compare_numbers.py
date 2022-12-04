def solution(num1: int, num2: int) -> int:
    """
    >>> solution(2, 3)
    -1
    >>> solution(11, 11)
    1
    >>> solution(7, 99)
    -1
    """
    if num1 == num2:
        return 1
    return -1
