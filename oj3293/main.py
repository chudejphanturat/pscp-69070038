"""Big Frame"""
def main():
    """big frame"""
    pic = []
    long = 0
    for _ in range(5):
        a = input().strip()
        pic.append(a)
        if len(a) > long:
            long = len(a)
    print("*" * (long + 4))
    for i in range(5):
        print(f"* {pic[i]:<{long}} *")
    print("*" * (long + 4))
main()
