def solution(n,k):
    output = [x for x in range(1, n+1)]

    while len(output) > 1:
        delete_item = (k - 1) % len(output)
        output.remove(output[delete_item])
        output = output[delete_item:] + output[:delete_item]
        

    return output

           
print(solution(7,3))

print('0')
        


