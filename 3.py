print("List Built-In Functions:\n 1. Length of List \n 2. Append function \n 3. Sort function \n 4. Insert function \n 5. Reverse Function \n 6. Pop function \n 7. Exit \n ")
lst = []
x=int(input("Enter the number of elements in List"))
print("Enter", x , "Items")
for i in range(x):
      v=input()
      lst.append(v)
print("The items of the List are", lst)
while(1):
    n=int(input("Enter your Choice: "))
    if(n==1):
        print("Length of the List is:",len(lst))
    elif (n==2):
        print("Enter the element to append")
        lst.append(input())
        print("The items of the List are", lst)
    elif (n==3):
        print("Sorting the list")
        lst.sort()
        print("The items of the Sorted List are", lst)
    elif (n==4):
        print("Insert into list")
        p=int(input("Enter the position to insert"))
        a=input("Enter the Item")
        lst.insert(p,a)
        print("The items of the List are", lst)
    elif (n==5):
        print("Reverse of list")
        lst.reverse()
        print("The items of the List are", lst)
    elif (n==6):
        print("Delete item from the list")
        r=int(input("Enter the position to delete"))
        lst.pop(r)
        print("The items of the List are", lst)
    elif (n==7):
        print("Exited")
        break
    else:
        print("Invalid Choice")
