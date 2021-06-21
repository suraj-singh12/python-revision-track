import os
os.mkdir("tables")      # creating a new directory
os.chdir("./tables/")       # changing working directory to tables/ 

for i in range(2,21):       # loop for each table [2->20]
    filename = "table of "+str(i)+".txt"    # filename for ith table
    with open(filename,'w') as f:           # open file to write ith table
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")     # write the table

