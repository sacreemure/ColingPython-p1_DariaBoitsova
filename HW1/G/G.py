def solution(a, b):
    a2 = a[:]
    for b2 in b:
        if b2 not in a:
            a2.append(b2)
    return a2
