def solution(total):
    h = total % (60 * 24) // 60
    m = total % 60
    return f'{h} {m}'
