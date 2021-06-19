
def fahrenheit(celsius):
    return (celsius * (9/5) + 32)

celsius = float(input("Enter temperature in Celsius: "))
print("{:.2f}".format(fahrenheit(celsius)),"F")
