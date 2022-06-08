NAME_TO_CODE = {"Aqua": "#00ffff", "Black": "#000000", "Blue1": "#0000ff",
                "Blue4": "#00008b", "Brown1": "#ff4040", "Brown3": "#cd3333",
                "Cameo Pink": "#efbbcc", "Candy Apple Red": "#ff0800", "Caribbean Green": "#00cc99"}

name = input("Enter colour's name: ")
while name != "":
    if name in NAME_TO_CODE:
        print(name, "is", NAME_TO_CODE[name])
    else:
        print("unknown")
    name = input("Enter colour's name: ")
