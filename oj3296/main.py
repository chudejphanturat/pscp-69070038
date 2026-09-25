"""color"""
import math as m
def main():
    """color"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(3):
        print(m.floor((a[i] + b[i])/2), end = " ")
main()
