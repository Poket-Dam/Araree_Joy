# -*- coding: utf-8 -*-

n, m, s = map(int, input().split())
data = list(map(int, input().split()))
count = 0

#count 변수에 정답(조사해야 할 사람의 수) 저장
for height in range(n):
	if data[height] == m or data[height] == s:
		count = count + 1

print(count)
