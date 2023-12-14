CountTheVowelsInTheElements="is every rectangle also a square?"
D={'a':0,'e':0,'i':0,'u':0}
for char in CountTheVowelsInTheElements:
    if char in D.keys():
        D[char]+=1
print(D)
