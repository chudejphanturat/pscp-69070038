"""heron"""
import math
a = float(input())
b = float(input())
c = float(input())
s = float((a + b + c)/2)
ans = (s*(s - a)*(s - b)*(s - c))
print(f"{math.sqrt(ans):.3f}")
