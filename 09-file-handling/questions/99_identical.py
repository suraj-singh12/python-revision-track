file1 = "this.txt"
file2 = "copy_of_this.txt"

with open(file1,"r") as f:
    content1 = f.read()

with open(file2,"r") as f:
    content2 = f.read()

if content1 == content2:
    print(f"'{file1}' and '{file2}' are identical with same content.")
