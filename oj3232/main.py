"""frog"""
def main():
    """frog"""
    jump,goal = map(int , input().split())
    dis = 0
    r = 0
    while dis < goal and jump > 0:
        dis += jump
        jump -= 2
        r += 1
    if dis < goal:
        print(-1)
    else:
        print(r)
main()
