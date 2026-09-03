"""jon"""
def main():
    """jon"""
    n,k,t = map(int, input().split())
    count = 1
    now = 1
    while True:
        if now == t:
            break
        now = ((now - 1 + k) % n) + 1
        if now == 1:
            break
        count += 1
    print(count)
main()
