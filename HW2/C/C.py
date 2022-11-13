def solution(arr):
    output = arr.pop(0)
    while arr:
        arr = list(zip(*arr))
        arr.reverse()
        for i in arr[0]:
            output.append(i)
        arr.remove(arr[0])

    return output          

