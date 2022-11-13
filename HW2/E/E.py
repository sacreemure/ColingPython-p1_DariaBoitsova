def solution(a, b):
    most = max(a, b)
    least = min(a, b)
    if least == 0:
        return most
    else:
        return solution(least-1, most+1)