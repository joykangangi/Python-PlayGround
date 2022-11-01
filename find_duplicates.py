#Find and return duplicates from a python list
def get_duplicate(string_list: list):
    count = 0
    str0 = []
    for str in string_list:
       count = string_list.count(str)
       if (count != 1 and str not in str0 ):
         str0.append(str)
         
    if (count == 1):
        print("No duplicate")   
    else:
        print(str0)   

fruits = ['apple', 'orange','banana','apple', 'banana']
names = ['Yoda','Moses','Alex','Olof']
get_duplicate(fruits)
get_duplicate(names)
