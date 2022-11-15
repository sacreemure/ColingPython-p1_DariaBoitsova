#++++++++++++++++++++++++++ 1 задание

def square(n):
    output = {}
    for i in range(1, n+1):
        output[i] = i**2
    return output

print(square(6))

#++++++++++++++++++++++++++ 2 задание

print(list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000,3201))))
        
#++++++++++++++++++++++++++ 3 задание

print(list(filter(lambda x: x % 2 == 0, range(1000,3001))))

#++++++++++++++++++++++++++ 4 задание
from math import factorial

def factor():
    factors = list(map(lambda x: factorial(x), range(0, 51)))
    output = list(filter(lambda x: x % 3 == 0, factors))
    return output

print(factor())

#++++++++++++++++++++++++++ 5 задание

def delete_odds(lst):
    output = [x for x in lst if lst.index(x) % 2 == 0]
    return output

test_list = ['a', 'b', 'c', 'd', 'e', 'f']


#++++++++++++++++++++++++++ 6 задание

def return_sums(lst):
    strings = [str(x) for x in lst]
    output = []
    for i in strings:
        all_num = 0
        for num in i:
            all_num += int(num)
        if all_num < 10:
            output.append(i)
    return output

test_list = [510, 98, 420, 73, 12, 32]

print(return_sums(test_list))