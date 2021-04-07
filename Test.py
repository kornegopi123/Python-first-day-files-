import Agecalculator as age
import Comapre3numbers as num

name=input('Enter your name: ')
age1=int(input('Enter your age: '))

res_age=age.age_calc(name,age1)
print(name,'you will get 100 years on',res_age)
a=int(input('Enter a number '))
b=int(input('Enter a number '))
c=int(input('Enter a number '))
res_num=num.calculate_big(a,b,c)

print(res_num,'is a big number')