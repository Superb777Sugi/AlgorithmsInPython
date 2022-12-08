def solution(num_list: list) -> list:
    """
    >>> solution([1 2 3 4 5])
    [2, 3]
    >>> solution([1, 3, 5, 7])
    [0, 4]
    """
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer
