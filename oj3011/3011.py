"""color"""
A = str(input())
B = str(input())
color_list = []
color_list.append(A)
color_list.append(B)
if "Red" in color_list and "Blue" in color_list:
    print("Violet")
elif "Red" in color_list and "Yellow" in color_list:
    print("Orange")
elif "Blue" in color_list and "Yellow" in color_list:
    print("Green")
else:
    if color_list.count("Red") > 1:
        print("Red")
    elif color_list.count("Blue") > 1:
        print("Blue")
    elif color_list.count("Yellow") > 1:
        print("Yellow")
    else:
        print("Error")
