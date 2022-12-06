def solution(n: int) -> int:
    """
    >>> solution(6)
    1
    >>> solution(10)
    5
    >>> solution(4)
    2
    """
    pizza = 1
    while (pizza * 6) % n != 0:
        pizza += 1
    return pizza
