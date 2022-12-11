def solution(n, k):
    if n == 1:
        return 1
    elif n > 1:
        return (1 + (solution(n - 1, k) + k - 1) % n)
    
