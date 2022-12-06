def solution(price: int) -> int:
    """
    >>> solution(150000)
    142500
    >>> solution(580000)
    464000
    >>> solution(8000)
    8000
    """
    discount_rates = {500000: 0.2, 300000: 0.1, 100000: 0.05, 0: 0}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            answer = price - int(price * discount_rate)
            return answer
