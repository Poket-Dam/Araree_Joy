# -*- coding: utf-8 -*-

#두 수중에 더 큰 값을 반환하는 함수
def get_max(a, b):
	return a if a >= b else b
	
if __name__ == '__main__':
	a, b = [ int(w) for w in input().split() ]
	answer = get_max(a, b)
	print(answer)