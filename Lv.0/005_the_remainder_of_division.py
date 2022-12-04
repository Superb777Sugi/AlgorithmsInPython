def solution(num1: int, num2: int) -> int:
    """
    >>> solution(3, 2)
    1
    >>> solution(1, 5)
    0
    """
    answer = num1 % num2
    return answer
