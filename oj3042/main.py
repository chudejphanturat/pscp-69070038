"""divide by 10"""
number = int(input())
answer = ""
while number >= 0:
    number = (number // 10) * 10
    answer = answer + str(number) + " "
    number -= 10
print(answer)
