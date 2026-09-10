"""card"""
def main(card):
    """card"""
    dok = ""
    num = ""
    if card[-1] == "D":
        dok = "diamonds"
    elif card[-1] == "S":
        dok = "spades"
    elif card[-1] == "H":
        dok = "hearts"
    elif card[-1] == "C":
        dok = "clubs"

    if card[:-1] == "Q":
        num = "queen"
    elif card[:-1] == "J":
        num = "jack"
    elif card[:-1] == "K":
        num = "king"
    elif card[:-1] == "A":
        num = "ace"
    else:
        num = card[:-1]
    print(f"{num} of {dok}")
main(input().upper())
