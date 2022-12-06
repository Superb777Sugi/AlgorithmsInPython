def solution(slice: int, n: int) -> int:
	"""
	>>> solution(7, 10)
	2
	>>> solution(4, 12)
	3
	"""
	pizza = 1 
	while (pizza * slice) < n: 
		pizza += 1 
	return pizza