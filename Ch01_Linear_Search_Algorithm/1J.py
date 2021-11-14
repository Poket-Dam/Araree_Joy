# -*- coding: utf-8 -*-

def range_sum_from_one(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum

def get_answer(n):
	sum = 0
	for i in range(1,n+1):
		sum += range_sum_from_one(i)
	return sum


if __name__ == "__main__":
	n = int(input())
	answer = get_answer(n)
	print(answer)