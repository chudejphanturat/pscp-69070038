"""Flight"""
def main():
    """Flight"""
    form,to = map(str, input().split())
    weight = float(input())
    if form == "BKK" and to == "CNX":
        print(f"{10 + (30 * weight):.2f}")
    elif form == "CNX" and to == "UBP":
        print(f"{15 + (40 * weight):.2f}")
    elif form == "UBP" and to == "BKK":
        print(f"{20 + (40 * weight):.2f}")
    elif form == "BKK" and to == "PKT":
        print(f"{25 + (50 * weight):.2f}")
    elif form == "PKT" and to == "CNX":
        print(f"{30 + (60 * weight):.2f}")
    elif form == "UBP" and to == "PKT":
        print(f"{40 + (70 * weight):.2f}")
    else:
        print("Error")
main()
