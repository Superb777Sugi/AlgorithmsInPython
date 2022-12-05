def solution(array: list) -> int:
    """
    >>> solution([1, 2, 3, 3, 3, 4])
    3
    >>> solution([1, 1, 2, 2])
    -1
    >>> solution([1])
    1
    """
    list = [0] * (max(array) + 1)
    for i in array:
        list[i] += 1
    answer = list.index(max(list))
    most_frequent_value = 0
    for i in list:
        if i == max(list):
            most_frequent_value += 1
            if most_frequent_value > 1:
                answer = -1
    return answer
