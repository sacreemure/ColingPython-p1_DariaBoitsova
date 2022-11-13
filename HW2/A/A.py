def solution(arr):
    max_len = 0
    current_len = 0
    last_item = None
    for i in arr:
        if last_item == None or last_item != i:
            last_item = i
            current_len = 0
        if last_item == i:
            current_len += 1
            if max_len <= current_len:
                max_len = current_len
    return max_len


