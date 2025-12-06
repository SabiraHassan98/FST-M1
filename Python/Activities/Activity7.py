#List Sum Calculator

#Activity 7, Write a Python program to calculate the sum of all the elements in a list. 
# Bonus points if you can make the user enter their own list
numbers = [1,2,3,4,5,6]
sum=0
print("the sequential sum is: ")
for number in numbers:
    sum = sum + number
    print(sum)

Sum=0 
numbers1 = input("enter a list of numbers: ").split()
for number in numbers1:
    Sum = Sum + int(number)
    number=Sum
print("The total sum of the elements is:", Sum)