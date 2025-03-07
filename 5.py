marks={}
n=int(input("Enter the number of students"))
for i in range(n):
    student_name=input("Enter student's name:")
    student_mark=input("Enter student's mark:")
    marks[student_name.title()]=student_mark
print("\nOriginal Dictionary=",marks)
smarks=sorted(marks.items())
print("Sorted Dictionary in Ascending=",smarks)

kmarks=sorted(marks.keys())
print("\nSorted Dictionary keys in Ascending=",kmarks)

vmarks=sorted(marks.values())
print("Sorted Dictionary values in Ascending=",vmarks)
