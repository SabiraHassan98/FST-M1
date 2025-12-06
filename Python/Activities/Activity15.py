#Write a Python program that throws a NameError.

#Handle the error so it doesn't halt execution.

try: 
    print(x)
except NameError:
    print("x hasn't been defined yet.")

#finally:
  #  print("this block will always execute")
  	
#else:
 # print("Nothing went wrong") 