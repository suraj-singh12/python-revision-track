s = input("Enter your comment: ")
all_spam = ["make a lot of money","buy now","subscribe this","click this"]

for spam in all_spam:
    if spam in s:
        print("This comment is a Spam!! as it contains '",spam,"'")
        break
else:
    print("It's spam free comment.")