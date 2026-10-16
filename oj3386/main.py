"""Dup"""
def main():
    """Dup"""
    an = int(input())
    bn = int(input())
    a = set()
    b = set()
    for _ in range(an):  
        enter = input()
        a.add(enter)
    for _ in range(bn):
        enter = input()
        b.add(enter)
    if not a.intersection(b):
        print("Nope")
    else:
        ans = sorted(a.intersection(b), reverse=True)
        for i in ans:
            print(i)
main()
