"""Ink"""
import math as m
def main():
    """find area of house then divide by area"""
    enter = input().split()
    area = int(enter[0])
    n = int(enter[1])
    for _ in range(n):
        house = input().split()
        x = int(house[0])
        y = int(house[1])
        ans = m.ceil(3.1416 * (((m.dist((x, y), (0, 0))) ** 2)) / area)
        #time(second) = ans
        print(ans)
main()
