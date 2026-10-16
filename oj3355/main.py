"""shorten"""
def main():
    """shorten"""
    num = []
    ans = []
    def enter(start,stop):
        """ansenter"""
        if start == stop:
            return ans.append(start)
        return ans.append(f"{start}-{stop}")
    while True:
        a = int(input())
        if a == -1:
            break
        num.append(a)
    if not num:
        return
    start,stop = num[0],num[0]
    for i in range(1,len(num)):
        if num[i] == stop+1:
            stop = num[i]
        else:
            enter(start,stop)
            start,stop = num[i],num[i]
    enter(start,stop)
    print(*ans ,sep=", ")
main()
