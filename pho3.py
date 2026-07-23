"""Quadrant"""
X = int(input())
Y = int(input())

if not X and not Y:
    print("O")

elif not X and Y:
    print("Y")

elif X and not Y:
    print("X")

elif X > 0 and Y > 0:
    print("Q1")

elif X > 0 > Y:
    print("Q4")

elif X < 0 < Y:
    print("Q2")

elif X < 0 and Y < 0:
    print("Q3")
