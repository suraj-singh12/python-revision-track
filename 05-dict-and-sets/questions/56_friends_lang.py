l = ["Fury","Tiger","Tony","Michael","Charles"]
langDict = dict()
for name in l:
    print("Hey",name,"! Enter your favourite language: ")
    lang = input().strip()
    langDict[name] = lang

print("Hi!, your favourite languages are as follows: ")
print(langDict)
