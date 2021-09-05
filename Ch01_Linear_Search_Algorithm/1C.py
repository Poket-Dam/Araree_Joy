# -*- coding: utf-8 -*-

#배열(data)의 원소 중 가장 큰 정수를 반환하는 함수를 작성해보자
def get_max(data, n):
	dataArr = list(data)
	maxNum = 0
	for i in range(n):
		if dataArr[i] > maxNum:
			maxNum = dataArr[i]
	return maxNum


#데이터의 수를 입력받는다
n = int(input())
#데이터들을 입력받는다
data = map(int, input().split())
#배열의 최대값을 저장한다 
answer = get_max(data, n)
#답을 출력한다
print(answer)