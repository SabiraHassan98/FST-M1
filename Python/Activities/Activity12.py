#
#def my_function():
#  print("Hello from a function") 
#my_function()

# Define function to calculate sum

def calculate_sum(n):
    if n <= 1:
        return n
    else :
        return n + calculate_sum(n-1)
# when user enters a number   
print ("-------when user enters a number -------") 
num = int(input("Enter a number: "))  
calculate_sum(num)
print(calculate_sum(num))

print("-----when num value is declared as 4----")
num = int(4) 
calculate_sum(num)
print(calculate_sum(num))

