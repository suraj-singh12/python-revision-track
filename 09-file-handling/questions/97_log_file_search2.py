
with open("logfile.log","r") as f:
    line_no = 0
    for line in f.readlines():
        line_no = line_no + 1
        if "python" in line.lower():
            print(f"Found python in line no: {line_no}")
    