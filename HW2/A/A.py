def solution(arr):
    max_len = 1
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 1
        
    return max_len


