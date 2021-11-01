# -*- coding: utf-8 -*-

def get_indexes(schools, n):
	first_index = -1
	last_index = -1
	for forward_searched_idx in range(len(schools)):
		if schools[forward_searched_idx] == "AJOU":
			first_index = forward_searched_idx+1
			break;
		
	for backstep_searched_idx in range(len(schools)-1,-1,-1):
		if schools[backstep_searched_idx] == "AJOU":
			last_index = backstep_searched_idx+1
			break;
	
	return first_index,	last_index
	
	
if __name__ == '__main__':
	n = int(input())
	schools = [ input() for i in range(n) ]
	first_index, last_index = get_indexes(schools, n);
	print( "{} {}".format( first_index, last_index) )