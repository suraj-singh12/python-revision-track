# when the condition becomes false, the else part of the for loop is executed.

# i goes from 0->4; so valid. As soon i becomes 5, it is out of range, so goes in else part of for loop
for i in range(5):
    print(i)
else:
    print("Done")

print()
# i goes from 0->4; so valid. But as soon i becomes 2, the loop is terminated suddenly because of break
# So the condition never became invalid, so else part is not executed.
for i in range(5):
    print(i)
    if (i==2):
        break
else:
    print("Done")

# in short:
# The else part of the for loop is executed only when the loop terminates successfully after completion