#Create a Python dictionary that contains a bunch of fruits and their prices.

#Write a program that checks if a certain fruit is available o

fruit_store_dict ={
    "apple": 90,
    "banana": 50,
    "chickoo": 55,
    "kiwi": 120
}

Ask = input("Please neter a fruit name: ").lower()
for i in fruit_store_dict:
    if Ask in fruit_store_dict:
        print(Ask, "fruit is avavilable")
        break;
    else:
        print(Ask, "is not available") 
        break;   