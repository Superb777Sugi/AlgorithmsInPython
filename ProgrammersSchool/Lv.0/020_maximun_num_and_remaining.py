def solution(money: int) -> list:
    """
    >>> solution(5500)
    [1, 0]
    >>> solution(15000)
    [2, 4000]
    """
    answer = [money // 5500, money % 5500]
    return answer
