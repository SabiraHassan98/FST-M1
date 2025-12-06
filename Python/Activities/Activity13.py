#Write a function sum() such that it can accept a list of elements and print the sum of all elements

print("Example1")
def calculate_sum1(num):
    sum=0
    for i in num:
        sum=sum+i
    return sum
    
list1 = [1,2,3,4,5,6,7,8,9,10]    
print(calculate_sum1(list1))    
#print((res))

#=========================================================

# Custom function to calculate sum
print("Example2")
def calculate_sum(numbers):
	sum = 0
	for num in numbers:
		sum += num
	return sum

# Define the list of numbers
numList = [10, 40, 60, 90]

# Call the sum() function with numList as argument
result = calculate_sum(numList)

# Print result with message
print(str(result))
    