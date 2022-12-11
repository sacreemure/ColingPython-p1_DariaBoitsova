def solution(arr):
    newarr = []
    
    while arr:
        newarr.append(arr.pop(0))
        arr = list(map(list, zip(*arr)))[::-1]
        
    return [j for i in newarr for j in i]
