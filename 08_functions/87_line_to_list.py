def remove_and_split(line, word):
    newLine = line.replace(word,"")
    newLine = newLine.split()
    return newLine

line1 = "       This is a line   with   many    spaces.   "
print(remove_and_split(line1,"many"))