PrintTheString=list("Don't panic!")
PrintTheString.pop(0)
PrintTheString.pop(2)
PrintTheString.pop(6)
PrintTheString.pop(6)
PrintTheString.pop(6)
PrintTheString.pop(6)

PrintTheString.insert(2,(PrintTheString.pop(3)))

print(PrintTheString)