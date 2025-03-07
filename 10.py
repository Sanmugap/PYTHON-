def readcontent():
    for i in list(open("data.txt","r")):
        print(i.rstrip())
def count():
    with open("data.txt","r")as fl:
        data=fl.read()
        cnt_ucase=0
        cnt_lcase=0
        cnt_digits=0
        for ch in data:
            if ch.islower():
                cnt_lcase+=1
            if ch.isupper():
                cnt_ucase+=1
            if ch.isdigit():
                cnt_digits+=1
        print("Total number of upper case letters are:",cnt_ucase)
        print("Total number of lower case are:",cnt_lcase)
        print("Total number of digits are:",cnt_digits)
        fl.close()
def search():
    cnt=0
    word_search=input("Enter the words to search:")
    with open("data.txt","r") as fl:
        for data in fl:
            words=data.split()
            for word in words:
                if (word==word_search):
                    cnt+=1
    print(word_search,"found",cnt,"times from the file")
def append():
    text=input("Enter text to append in the file:")
    with open ("data.txt","a")as fl:
        fl.write("\n")
        fl.write(text)
        fl.close()
print("================================================")
print("1.Read the contents of file")
print("2.Countthe total number of uppercase,lowercase and digits")
print("3.Find the total occurences of a specific word")
print("4.Append the contents")
print("5.Exit")
print("==================================================")
while(1):
    choice=int(input("Enter your choice:"))
    if choice==1:
        readcontent()
    elif choice==2:
        count()
    elif choice==3:
        search()
    elif choice==4:
        append()
    elif choice==5:
        print("Exited")
        break
    else:
        print("wrong choice")
