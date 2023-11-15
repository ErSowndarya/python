#Rule2: Any positional argument cannot follow any keyword argument
print("Hello","World")
print("World","Hello")
#Error because positional arguments cannot follow keyword arguments
print(sep="$","Hello","World")