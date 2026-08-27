"""divide"""
def main():
    """divide"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    ans = 0
    for a in range(a,b+1):
        if (a % c) == d:
            ans += 1
    print(ans)
main()
