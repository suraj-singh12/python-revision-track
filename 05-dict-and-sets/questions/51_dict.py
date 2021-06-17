dict1 = {
    "kitab":"Book",
    "ghar":"Home",
    "kursi":"Chair",
    "mej":"Table",
    "deewar":"Wall"
}
print("Enter the Hindi word out of: ")
print(list(dict1.keys()))

print()
word = input()

if dict1.get(word) is not None:
    print("The meaning of " + word + " is:",end = ' ')
    print(dict1.get(word))
else:
    print("Error!!, there is no such word as "+word+" in the dictionary.")
