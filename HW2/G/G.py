def solution(a, b):

    b = list(filter(lambda x: x not in a, b))

    output = []

    index_1 = 0
    index_2 = 0

    while index_1 < len(a) and index_2 < len(b):
        if a[index_1] < b[index_2]:
            output.append(a[index_1])
            index_1 += 1
        else:
            output.append(b[index_2])
            index_2 += 1

    a = list(filter(lambda x: x not in output, a))
    b = list(filter(lambda x: x not in output, b))

    output = output + a + b
    
    return output
          
test_1 = [2, 3, 3, 5, 7, 11, 13, 16, 20, 21, 22, 22, 27, 27, 29, 33, 34, 37, 40, 40, 41, 43, 45, 51, 55, 55, 56, 59, 60]
test_2 = [5, 6, 8, 12, 57]

print(solution(test_1, test_2))