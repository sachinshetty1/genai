num1 =int(input("First Number ")); #100
num2 =int(input("Second Number ")); #300
num3 =int(input("Third Number ")); #200

  #  100 >=200 and 100 >=300 
if num1 >= num2 and num1 >= num3 : 
     largest=num1 
elif num2 >= num1 and num2 >= num3 :
    largest= num2;
else : 
    largest= num3;

print("The largest number is", largest);

