
# file = open("textFile.txt",'r')
# content = file.read()
# print(content)
# file.close()


# a better one
try:
    file = open("textFile.txt",'r')
except IOError:
    print("Error Reading the file!!, check if the file exists or not.")
    exit()

content = file.read()   # reads whole content of the File textFile.txt in one go
# content = file.read(5)          # will read only first 5 characters from the File of textFile.txt
# content = file.readline()       # reads one line at a time
# content = file.readlines()      # reads all lines and makes a list of them
print(content)
file.close()