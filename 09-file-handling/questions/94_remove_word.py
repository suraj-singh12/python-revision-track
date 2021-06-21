# short way to do it
with open("myfile1.txt","r") as f:
    content = f.read()
content = content.replace("wrong","$%@^$^#")

with open("myfile1.txt","w") as f:
    f.write(content)


# try:                    # safely check if file exists
#     f = open("myfile1.txt","r")

# except FileNotFoundError:         # if does not exists, create a file
#     with open("myfile1.txt","w") as f:
#         pass
#     print("File is empty!!")        # as we have just created it,  it did not exist
#     exit()

# to_remove = "wrong"
# lines = f.readlines()
# f.close()

# new_content = ''
# for line in lines:
#     for word in line.split():
#         if word.lower() == to_remove.lower():
#             new_content = new_content + ' #####'
#         else:
#             new_content = new_content + ' ' + word
#     new_content = new_content + '\n'

# with open("myfile1.txt","w") as f:
#     f.write(new_content)