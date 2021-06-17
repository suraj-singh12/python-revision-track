data = input ("Enter any type value: ")
if data.isdigit() == True:
    print("Numeric data entered.")
elif data.isalpha() == True:
    print("String data entered.")
elif data.isalnum() == True:
    print("Alphanumeric data entered.")