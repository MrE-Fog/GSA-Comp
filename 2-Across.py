sub_count_1 = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}

sub_count_2 = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}

total_count = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}


def solution(s, x, y):
    n = len(s)
    multiplier = (y-x)//n
    for i in range(0, n):
        sub_count_1[s[i%n]] += 1
    if x%n > y%n:
        r = range(y%n, (x%n)+1) 
    else:
        r = range(x%n, (y%n)+1)
    for i in r:
        sub_count_2[s[i%n]] += 1
    for k in sub_count_1:
        total_count[k] = (sub_count_1[k]*multiplier) + sub_count_2[k]
    m = max(total_count, key=total_count.get)
    for k in total_count:
        if k is not m and total_count[k] == total_count[m]:
            return 0
    return total_count[m]

if __name__ == '__main__':
    s = 'ATTTA'
    print solution(s, 3, 10)
