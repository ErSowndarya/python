PrintALocation = 5

PrintBLocation = PrintALocation

print("#1")
print("Value of a =", PrintALocation, "and location of a is:", id(PrintALocation))
print("Value of b =", PrintBLocation, "and location of b is:", id(PrintBLocation))

a = 7

print("#3")
print("Value of a =", PrintALocation, "and location of a is:", id(PrintALocation))
print("Value of b =", PrintBLocation, "and location of b is:", id(PrintBLocation))