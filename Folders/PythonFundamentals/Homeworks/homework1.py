#Homework
#Create a list that contains all the even numbers between 1 and 299.


list=[]
for i in range(1,299,2):
  list.append(i)
  print(len(list))
print(list)
#Iterate through the previously created list and print first the length of the list then all the squared values of the list.
list2=[]
for value in list:
    print(len(list))
    list2.append(value**2)
    print(list2)
#In one line check if 57 is in the list using one line of python.
print(57 in list)
