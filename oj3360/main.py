"""Bread"""
def main():
    """Bread"""
    w,h,m,n = map(int,input().split())
    mlist = [0,w]
    nlist = [0,h]
    mlist[1:1] = map(int,input().split())
    nlist[1:1] = map(int,input().split())
    m+=1
    n+=1
    def cut(a):
        for i in range(len(a) - 1):
            a[i] = a[i + 1] - a[i]
        a.pop()
        a.sort(reverse=True)
        return a[0:2]
    nlist = cut(nlist)
    mlist = cut(mlist)
    ans = [mlist[0]*nlist[0],mlist[1]*nlist[1],mlist[0]*nlist[1],mlist[1]*nlist[0]]
    ans.sort(reverse=True)
    print(ans[0],ans[1])
main()
