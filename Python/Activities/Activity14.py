#Fibonacci Numbers

def fibon(number):
    if number<=1:
        return number
    else:
        return (fibon(number-1)+fibon(number-2))
    
num = int(input("Please enter a number: "))


if num<=0:
    print("Please enter a positive number ")
else:
    print("fibonaccie series: ") 
    for i in range(num):
      print(fibon(i))    

