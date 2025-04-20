#wieight converter 
#A simple weight converter program that converts input weight from kg to lb depending on what the user wants

weight = input("What do you weigh?: ")
weight_unit = input("(L)bs or (K)g: ")
weight_kg = float(weight) * 2.205
weight_lbs = float(weight) * 0.453592


if weight_unit == 'L' or weight_unit == 'l':
    print(weight_lbs)
    print("You have converted from lbs to kg")
elif weight_unit == 'K' or weight_unit == 'k':
    print(weight_kg)
    print("Ypu have converted from kg to lbs")
else:
    print("check input og unit of measurement")