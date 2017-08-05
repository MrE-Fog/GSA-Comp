import math

def solution(t):
	out = ''
	for (N,D) in t:
		out += str(int(math.ceil(math.ceil(math.log(N)/math.log(2))/D)))
	return out


if __name__ == '__main__':
	print solution(((100000, 2), (12345, 4), (121212, 3), (643125, 7), (1000000, 10), (1, 1), (123123, 4), (432765, 2), (10000, 9), (1, 10)))