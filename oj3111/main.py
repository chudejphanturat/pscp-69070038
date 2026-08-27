"""School store"""
import math as m
def main(mem,n):
    """Store"""
    total = 0
    discount = 1
    for _ in range(n):
        total += float(input())
    if mem == "Y":
        discount = 0.95
    elif total >= 500:
        discount = 0.97
    ans = total * discount
    if (ans*100)-m.floor(ans) > 0.48:
        ans = (m.ceil(ans*100))/100
    print(f"{ans:.2f}")
main(input(),int(input()))
