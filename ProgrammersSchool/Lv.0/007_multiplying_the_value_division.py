def solution(num1: int, num2: int) -> int:
    """
    >>> solution(3, 2)
    1500
    >>> solution(7, 3)
    2333
    >>> solution(1, 16)
    62
    """
    answer = int((num1 / num2) * 1000)
    return answer
