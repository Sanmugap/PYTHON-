from functools import reduce
def fahrenheit(T):
    return(float(9)/5*T+32)
def celsius(T):
    return(float(5)/9)*(T-32)
temperatures=(36.5,37,37.5,38,39)
F=map(fahrenheit,temperatures)
C=map(celsius,F)
temperature_in_fahrenheit=list(map(fahrenheit,temperatures))
temperature_in_celsius=list(map(celsius,temperature_in_fahrenheit))
print(temperature_in_fahrenheit)
print(temperature_in_celsius)
filter_result=list(filter(lambda x:x>=37 and x<=38,temperatures))
print(filter_result)
reduce_result=reduce(lambda num1,num2:num1*num2,temperatures)
reducesum=reduce(lambda num1,num2:num1-num2,temperatures)
print(reduce_result)
print(reducesum)
