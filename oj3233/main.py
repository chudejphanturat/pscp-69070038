"""Lottery"""
def main():
    """Lottery"""
    prize = 0
    a1,a2 = input().split()
    b1,b2 = input().split()
    #num
    if a2 == b2:
        prize = 100000
    elif a2[-3:] == b2[-3:]:
        prize = 200
    elif a2[-2:] == b2[-2:]:
        prize = 100
    #letter
    if a1 == b1 and not prize:
        prize = 20
    elif a1 == b1:
        prize *= 10
    print(prize)
main()
