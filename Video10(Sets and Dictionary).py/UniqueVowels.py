#print all the unique vowels 
PrintTheVowelsInTheElements="is every rectangle also a square?"
Vowels=list("aeiou")
prev_char=[]
for char in PrintTheVowelsInTheElements:
    if char in Vowels:
        if char not in prev_char:
         print(char)
        prev_char.append(char)

print(prev_char)
