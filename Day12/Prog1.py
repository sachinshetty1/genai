fruits = ["Apple", "Mango", "Banana",100] # LIST  we have multiple ready methods 
print(fruits);      # apple , mango, banana 
print(fruits[0]);   # Apple 
print(fruits[1]);   #mango 
print(fruits[-1]);  
fruits.append("Orange");    #adds at the end 
print(fruits);
fruits.insert(1,"Grapes");  #adds at index 1 
print(fruits);
fruits[0]="WaterMelon";
print(fruits);
fruits.remove("Banana");
print(fruits); #remove the value
fruits.pop();
print(fruits);
fruits.pop(1);
print(fruits);
del fruits[1];
print(fruits);
fruits.extend(["Jackfruit","PineApple"]);
print(fruits);
print("============");
for fruit in fruits :
        print(fruit)
print("================");
if "WaterMelon" in fruits:
    print("yes WaterMelon is Avlaible")

print("-------------")
fruits.clear();
print(fruits);
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

