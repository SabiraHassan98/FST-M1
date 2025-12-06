# Given a list of numbers, return True if first and last number of a list is same.

list_a = input("Enter a list of numbers: ").split()
print(list_a) # to check how split works
firstElement= list_a[0]
lastElement= list_a[-1]
if firstElement == lastElement:
    print("True")
else:
    print("False")

