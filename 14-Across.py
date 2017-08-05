def solution(tuple_of_test_cases):
    out = ''
    for test in tuple_of_test_cases:
        num_platforms = test[0]
        jump_range = test[1]
        distances = list(test[2])
        count = 0
        for i in range(0, num_platforms):
            if distances[i] > jump_range:
                distances[i+1] += distances[i] - jump_range
                distances[i] = jump_range
                count += 1
        if distances[num_platforms] <= jump_range:
            out += str(count)
        else:
            count = 0
            distances = list(test[2][::-1])
            for i in range(0, num_platforms):
                if distances[i] > jump_range:
                    distances[i+1] += distances[i] - jump_range
                    distances[i] = jump_range
                    count += 1
            if distances[num_platforms] <= jump_range:
                out += str(count)
    return out



if __name__ == '__main__':
    print solution(((7, 3, (4, 3, 3, 3, 3, 3, 3, 2)), (4, 3, (1, 2, 3, 4, 5)), (3, 1, (2, 2, 2, 2)), (3, 2, (1, 2, 2, 2))))