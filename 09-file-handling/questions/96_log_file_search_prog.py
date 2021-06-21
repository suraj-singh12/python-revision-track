with open("logfile.log","r") as f:
    content = f.read().lower()

if "python" in content:
    print("Yes! python exists in the log file.")
else:
    print("NO! python is not present in the log file.")