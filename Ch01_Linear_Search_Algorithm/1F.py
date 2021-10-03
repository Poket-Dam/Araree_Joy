# -*- coding: utf-8 -*-

def find_value(value, arr):
	index = -1
	for i in range(len(arr)):
		if arr[i] == value :
			index = i
	return index

n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = find_value(m, data)
print(answer)