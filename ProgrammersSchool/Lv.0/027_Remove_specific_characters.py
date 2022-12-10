def solution(string: str, letter: str) -> str:
    """
    >>> solution("abcdef", "f")
    "abcde"
    >>> solution("BCBdbe", "B")
    "Cdbe"
    """
    return string.replace(letter, "") 
  
  
def solution1(string: str, letter: str) -> str:
    """
    >>> solution("abcdef", "f")
    "abcde"
    >>> solution("BCBdbe", "B")
    "Cdbe"
    """
    list = [] 
    for i in string: 
        if i != letter: 
            list.append(i) 
    answer = "".join(list)
    return answer
  
