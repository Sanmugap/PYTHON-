import string
print("String functions:\n1.String length\n2.Ends with finction\n3.Find function\n4.Capitalize,uppercase,lowercase function\n5.Exit\n")
while(1):
    n=int(input("Enter your choice"))
    if (n==1):
        str=input("Enter a string:")
        print("Length of the string is:",len(str))
    elif(n==2):
        str=input("Enter a string:")
        x=str.endswith(".")
        print("The string ends with .",x)
    elif(n==3):
        str1=input("Enter ther first string:")
        x=str1.find(input("Enter the string to find"))
        if x>0:
            print("Found")
        else:
            print("Not found")
    elif(n==4):
        str1=input("Enter the first string:")
        print("Capitalize:",(str1.capitalize()))
        print("Upper case:",(str1.upper()))
        print("Lower case:",(str1.lower()))
    elif(n==5):
        print("Exited")
        break
    else:
        print("Invalid choice")
