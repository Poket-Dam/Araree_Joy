# -*- coding: utf-8 -*-

def find_index(data, n):
	average = sum(data)/n
	closed_idx = -1
	min_difference = 100010
	for i in range(len(data)):
		difference = abs(average - data[i])
		if difference < min_difference: 
			closed_idx = i
			min_difference = difference
	return closed_idx + 1

if __name__ == "__main__":
	n = int(input())
	data = [ int(w) for w in input().split() ]
	answer = find_index(data, n)
	index = answer-1
	print("{} {}".format(answer, data[index]))