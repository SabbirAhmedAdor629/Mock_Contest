#include<stdio.h>
a =int(input("Enter number: "));
b =int(input("Enter number: "));
c =int(input("Enter number: "));

result = a+b*c;
result2 = a+(b*c);
result3 = a*b*c;
result4 = (a+b)*c;

if (result >= result2) & (result  >= result3) & (result  >= result4):
    print(result);

elif (result2  >=  result) & (result2  >= result3) & (result2  >= result4):
    print(result2);
    
elif (result3  >=  result) & (result3 >= result2) & (result3 >= result4):
    print(result3);
    
else: 
    print(result4);

