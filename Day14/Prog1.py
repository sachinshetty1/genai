# [ ]
# order  : user enterted order
#duplicate ? : yes will allow duplciate  
arr = [30, 30, 20, 100, 50, 60, 35, 80]
print("Original List:", arr)

# sorted  : merge , selection , quick,bubble 

# Ascending order
ascending = sorted(arr)
print("Ascending:", ascending)

# Descending order
descending = sorted(arr, reverse=True)
print("Descending:", descending)

# Remove duplicates using set
unique_values = list(set(arr))
print("Without Duplicates:", unique_values)


# Remove duplicates and sort ascending
unique_ascending = sorted(set(arr))
print("Unique Ascending:", unique_ascending)

# Remove duplicates and sort descending
unique_descending = sorted(set(arr), reverse=True)
print("Unique Descending:", unique_descending)


#Original List:
#Ascending: 
#Descending: 
#Reversed:
#Without Duplicates: order is not guaranteed
#Unique Ascending: 
#Unique Descending
