# -*- coding: utf-8 -*-

def solve(data, n, p, q):
	canRidePeopleList = []
	for weight in data:
		if weight <= p :
			canRidePeopleList.append(weight)
	
	S = sum(canRidePeopleList) #이 변수에 탑승할 수 있는 회원의 몸무게의 합을 계산한다
	C = len(canRidePeopleList) #이 변수에 탑승할 수 있는 사람의 수를 계산한다
	print(C, S)
	
	canEveryoneRide = 'NO';
	if S <= q :
		canEveryoneRide = 'YES'
	print(canEveryoneRide)

if __name__ == "__main__":
	n, p, q = [ int(w) for w in input().split() ]
	data = [ int(w) for w in input().split() ]
	solve(data, n, p, q)
