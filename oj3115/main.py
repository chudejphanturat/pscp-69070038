"""Arcade of Time: Store Check"""
def main():
    """Arcade of Time: Store Check"""
    nstore,ntime = input().split()
    nstore,ntime = int(nstore),int(ntime)
    opened = []
    close = []
    ans = []
    for _ in range(nstore):
        a,b = input().split()
        a,b = int(a),int(b)
        opened.append(a)
        close.append(b)
    time = input().split()
    for j in range(ntime):
        score = 0
        for i in range(nstore):
            if opened[i] <= int(time[j]) <= close[i] - 1:
                score += 1
        ans.append(score)
    print(*ans,sep=" ")
main()
