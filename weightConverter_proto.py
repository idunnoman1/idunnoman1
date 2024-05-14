#--nah bro im finishing this later--

#mg to g
#mg to kg

#g to kg
#g to mg

#kg to g
#kg to mg

weight = float(input("what is your weight"))
fromUnit = input("what do you want to convert from")
toUnit = input("what do you want to convert to")

if fromUnit == "mg" and toUnit == "g":
    newWeight = round(weight / 1000, 2)
    print(newWeight)
