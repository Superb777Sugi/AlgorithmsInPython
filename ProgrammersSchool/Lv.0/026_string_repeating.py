def solution(string: str, n: int) -> str: 
    """
    >>> solution("hello")
    "hhheellllllooo"
    """
    repeated_string = [] 
    for i in string: 
        repeated_string.append(i * n) 
    return "".join(repeated_string)
