# -*- coding: utf-8 -*-

def get_sum(data, n):
	answer = sum(data[0:n])
	return answer


if __name__ == '__main__':
	n = int(input())
	data = [ int(w) for w in input().split() ]
	answer = get_sum(data, n)
	print(answer)