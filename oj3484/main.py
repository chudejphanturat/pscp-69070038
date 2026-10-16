"""tile"""
def main():
    """tile"""
    n,fine = list(map(int,input().split()))
    tile = []
    anscount = []
    ans = []
    count = 0
    for _ in range(n):
        enter = list(map(int,input().split()))
        tile.append(enter)
    for i in range(n):
        print(*tile[i], end=" ")
        print(sum(1 for x in tile[i] if x > 0), sum(tile[i]))

    for k in range(n):
        for j in range(n):
            if tile[j][k] > 0:
                count += 1
        anscount.append(count)
        count = 0
    print(*anscount)
    for k in range(n):
        for j in range(n):
            if tile[j][k] > 0:
                count += tile[j][k]
        ans.append(count)
        count = 0
    print(*ans)
    print(f"{sum(anscount)} {sum(ans)} {sum(ans) * fine:.2f}")
main()
