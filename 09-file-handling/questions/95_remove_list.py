with open("myfile2.txt","r") as f:
    content = f.read()

to_remove = ['twinkle','star','dismiss','done']
for word in to_remove:
    content = content.replace(word,"@#$%#$^")

with open("myfile2.txt","w") as f:
    f.write(content)