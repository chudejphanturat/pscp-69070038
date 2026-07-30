"""Temperature"""

def main():
    """turn into C then into {temp_into}"""
    celcius = float(input())
    temp_form = input()
    temp_into = input()
    #Def into Celcius
    def kelvin_celcius():
        return celcius - 273.15
    def farenheit_celcius():
        return ((celcius - 32) * 5) / 9
    def rankine_celcius():
        return ((celcius * 5) / 9) - 273.15
    #Def Into
    def kelvin():
        return celcius + 273.15
    def farenheit():
        return ((celcius * 9) / 5) + 32
    def rankine():
        return ((celcius + 273.15) * 9) / 5
    #turn into celcius
    if temp_form == "R":
        celcius = rankine_celcius()
    elif temp_form == "K":
        celcius = kelvin_celcius()
    elif temp_form == "F":
        celcius = farenheit_celcius()
    #turn into
    if temp_into == "R":
        print(f"{(rankine()):.2f}")
    elif temp_into == "K":
        print(f"{(kelvin()):.2f}")
    elif temp_into == "F":
        print(f"{(farenheit()):.2f}")
    elif temp_into == "C":
        print(f"{celcius:.2f}")
main()
