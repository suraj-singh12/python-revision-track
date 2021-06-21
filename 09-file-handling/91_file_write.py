
file = open("textFile.txt",'w')     # use 'a' for append mode
content = input("Enter content: ")
file.write(content)
file.close()
