"""Season"""
month = int(input())
day = int(input())
if not month % 3 and day >= 21:
    month+=1

if month <= 3 or month > 12:
    print("winter")
elif month <= 6:
    print("spring")
elif month <= 9:
    print("summer")
elif month <= 12:
    print("fall")
