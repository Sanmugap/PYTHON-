def test(lst_tuples):
    result=[list(el)for el in lst_tuples]
    return result
lst_tuples=[(1,2),(2,3),(3,4)]
print("Oringinal list of tuples:")
print(lst_tuples)
print("Convert the said list of a list of lists:")
print(test(lst_tuples))
lst_tuples=[(1,2),(2,3,5),(3,4),(2,3,4,2)]

print("\nOriginal list of tuples:")
print(lst_tuples)
print("Convert the said list of tuples to a list of lists:")
print(test(lst_tuples))

intTuple=()
number=int(input("Please enter the total tuple items to store="))
for i in range(1,number+1):
    value=int(input("Please enter%d binary tuple item="%i))
    intTuple+=(value,)

print("Tuples Items=", intTuple)
res=int("".join(str(ele)for ele in intTuple),2)

print("Decimal number is:"+str(res))
