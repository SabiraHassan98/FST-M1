#Tuple Number Checker

#Given a tuple of numbers, iterate through it and print only those numbers which are divisible by 5
num_tuple = (1,2,3,4,5,6,7,8,9,0)
        
for num in num_tuple:
    if num % 5 == 0:
        print(num)

#how to print as a tuple
print("---------displaying the output in tuple-------")
new_listby5 = []
for num in num_tuple:
    if num % 5 == 0:
        new_listby5.append(num)
#print("the list elements where remainder is 0 when devided ny 5: ", new_listby5)
new_tupleby5 = tuple(new_listby5)
print("The tuple elements which are divided by 5 are: ", new_tupleby5)
#new_list = list(new_tupleby5)
#print("the tuple conversion to list: ",new_list)
#new_list = set(new_tupleby5)
#print("the tuple/list conversion to set: ",new_list)