"""Giraffe"""
def main(n):
    """Giraffe"""
    group = []
    ans = 0
    for _ in range(n):
        group.append(int(input()))
    if n == 1:
        return 1
    for j in range(n):
        if not j and group[j]>group[j+1]:
            ans += 1
        elif j == len(group)-1 and group[j]>group[j-1]:
            ans += 1
        elif group[j-1] < group[j] > group[j+1]:
            ans += 1
    return ans
print(main(int(input())))
