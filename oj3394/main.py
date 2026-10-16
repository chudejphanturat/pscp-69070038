"""send"""
def main():
    """send"""
    n,t = map(int ,input().split())
    t = t-1
    send = []
    sended = set()
    for _ in range(n):
        send.append(int(input()))
    while True:
        if t in sended or t == -1:
            break
        sended.add(t)
        t = send[t]-1
    print(len(sended))
main()
