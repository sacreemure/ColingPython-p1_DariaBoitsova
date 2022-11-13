def solution(x):
    temp_string = x.replace('h', 'H', x.count('h') - 1)
    temp_string = temp_string.replace('H', 'h', 1)

    output = ''

    for i in range(len(x)):
        if i % 3 != 0 or i == 0:
            output = output + temp_string[i]
    
    output = output.replace('1', 'one')
    return output
