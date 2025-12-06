#Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list.
List1 = [1,2,3,4,5,6,7,8,9,10]
List2 = [11,12,23,24,45,44,56,7,8,9]

print("List one: ", List1)
print("List two: ", List2)

#for single list
#newList1 = []
#newList2 = []
#for num in List1:
#    if num % 2 != 0 :
#    newList1.append(num)
#    else:
#     newList2.append(num)     
#print("this is the odd list created from list 1: ", newList1)     
#print("This is the even list created from list1: ",newList2)

# creatig odd list from list1 and creating even list from list2
oddList1 =[]
for num in List1 :
  if num % 2 != 0:
    oddList1.append(num)

print ("here is the odd list from list1: ", oddList1)    

# for creating even list form list2
evenList2=[]
for i in List2:
  if i % 2 == 0:
    evenList2.append(i)

print("here is the even list from list2: ", evenList2)    