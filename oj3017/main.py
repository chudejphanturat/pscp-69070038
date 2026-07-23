"""Bill"""
FOOD = float(input())
FOOD1 = FOOD * 0.10
if FOOD1 <= 50:
    FOOD += 50
elif FOOD1 >= 1000:
    FOOD += 1000
else :
    FOOD += FOOD1
print(f"{FOOD * 1.07:.2f}")
