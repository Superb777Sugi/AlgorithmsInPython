def solution(n: int) -> int:
    """
    >>> solution(7)
    1
    >>> solution(1)
    1
    >>> solution(15)
    3
    """
    pizza = n // 7
    if (n % 7) == 0:
        pizza = pizza
    else:
        pizza = pizza + 1
    return pizza
