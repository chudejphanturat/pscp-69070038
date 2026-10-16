"""padthai"""
def main():
    """padthai"""
    padthai = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts"
    }
    goodtaste = {
        "Sweet",
        "Sour",
        "Salty"
    }
    cook = set()
    taste = set()
    while True:
        enter = input()
        if enter == "Cook":
            break
        cook.add(enter)
    while True:
        enter = input()
        if enter == "End":
            break
        taste.add(enter)

    if not cook.issubset(padthai):
        return "This is not Pad Thai!!!"

    if len(cook.intersection(padthai)) == len(padthai):
        if taste.issubset(goodtaste) and len(taste.intersection(goodtaste)) == len(goodtaste):
            return "Delicious!"
        return "Not Bad..."
    return "This is bad!"
print(main())
