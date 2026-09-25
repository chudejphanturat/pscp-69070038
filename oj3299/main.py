"""dokmai"""
def main():
    """dokmai"""
    l,n = map(int, input().split())
    back = 0
    row = 0
    cross = 0
    lamount = 1
    for f in range(1,l):
        back += f
    while n > cross:
        row += 1
        cross += (lamount * l) + back
        lamount += l
    print(row)
main()
