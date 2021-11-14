# -*- coding: utf-8 -*-

def find_min_index(data, begin, end):
	min_data = min(data[begin:end+1])
	return data.index(min_data) 

def selection_sort(data, n):
	for i in range(len(data)):
		min_index = find_min_index(data, i, len(data)-1)
		data[i], data[min_index] = data[min_index], data[i]

if __name__ == "__main__":
	n = int(input())
	data = [ int(w) for w in input().split() ]
	selection_sort(data, n)
	print(" ".join([str(w) for w in data]))