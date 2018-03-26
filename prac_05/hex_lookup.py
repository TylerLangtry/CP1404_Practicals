
hex_values = {"BLUE 1": "#0000ff", "GREEN 1": "#00ff00", "HOT PINK": "#ff69b4",
              "MAGENTA": "#ff00ff", "MEDIUM": "#66cdaa", "PALE": "#db7093",
              "RED 1": "#ff0000", "SALMON": "#fa8072", "SNOW 1": "#fffafa", "TAN": "#d2b48c"}

hex = input("Enter Colour: ").upper()
while hex != "":
    if hex in hex_values:
        print(hex, "is", hex_values[hex])
    else:
        print("Invalid Colour")
    hex = input("Enter Colour: ")
