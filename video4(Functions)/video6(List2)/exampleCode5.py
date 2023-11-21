# List is Mutable


a = [1,2]

b = a

print("#1")
print("Value of a =", a, "and location of a is:", id(a))
print("Value of b =", b, "and location of b is:", id(b))

a.extend(["hello","world"])

print("#2")
print("Value of a =", a, "and location of a is:", id(a))
print("Value of b =", b, "and location of b is:", id(b))



a = [3,2]

print("#3")
print("Value of a =", a, "and location of a is:", id(a))
print("Value of b =", b, "and location of b is:", id(b))