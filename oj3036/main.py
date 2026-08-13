"""pyramid"""
def main():
    """pyramid"""
    room = int(input())
    a = 1
    row = -1
    while room > a ** 2:
        a += 1
        row += 1
    if not row % 2:
        if not room % 2:
            print(((row) * 2) + 2)
        else:
            print(((row) * 2) + 1)
    else:
        if not room % 2:
            print(((row) * 2) + 1)
        else:
            print(((row) * 2) + 2)
main()
