converter = input("What converter do you want to use? (temp / length)")

if converter == "temp":
    print("Temperature Converter")

    temp = float(input("What temperature do you want to convert"))
    fromUnit = input("What do you want to convert from (c / f / k)")
    toUnit = input("What do you want to convert to (c / f / k)")

    if fromUnit == "c" and toUnit == "f":
        newTemp = round((9 * temp) / 5 + 32, 2)
        print(f"The temperature is {newTemp} degrees Fahrenheit")

    elif fromUnit == "c" and toUnit == "k":
        newTemp = round(temp + 273.15, 2)
        print(f"The temperature is {newTemp} Kelvins")

    elif fromUnit == "f" and toUnit == "c":
        newTemp = round((temp - 32) * 5 / 9, 2)
        print(f"The temperature is {newTemp} degrees Celsius")

    elif fromUnit == "f" and toUnit == "k":
        newTemp = round((temp - 32) * 5 / 9 + 273.15, 2)
        print(f"The temperature is {newTemp} Kelvins")

    elif fromUnit == "k" and toUnit == "c":
        newTemp = round(temp - 273.15)
        print(f"The temperature is {newTemp} degrees Celsius")

    elif fromUnit == "k" and toUnit == "f":
        newTemp = round((temp - 273.15) * 9/5 + 32, 2)
        print(f"The temperature is {newTemp} degrees Fahrenheit")

    elif fromUnit == "c" and toUnit == "c":
        print("Why would you convert Celsius to Celsius")

    elif fromUnit == "f" and toUnit == "f":
        print("Why would you convert Fahrenheit to Fahrenheit")

    elif fromUnit == "k" and toUnit == "k":
        print("Why would you convert Kelvin to Kelvin")

    else:
        print("Error")

elif converter == "length":
    print("Length converter")

    length = float(input("What is the length? \n"))
    unit = input("What unit do you want to convert to? (cm / in) \n")

    if unit == "cm":
        newLength = round(length * 2.54, 2)
        print(f"Your length is {newLength} cm")

    elif unit == "in":
        newLength = round(length / 2.54, 2)
        print(f"Your length is {newLength} in")
