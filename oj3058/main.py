"""brick"""
def main():
    """brick"""
    small = int(input())
    big = int(input())
    goal = int(input())
    ans = False
    big_use = goal // 5
    if big >= big_use:
        goal -= big_use * 5
        if small >= goal:
            ans = True
    else:
        goal -= big * 5
        if small >= goal:
            ans = True
    if ans:
        print(goal)
    else:
        print(-1)
main()
