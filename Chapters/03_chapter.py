# 1
friends=["Apple", "Samsung", "Andriod", "5", "34.5", "Ashar"]
print(friends[4])
# 2(Changing List elements)
friends[0]= "Low battery"
print(friends)
# List Items
print(friends[0:4])
friends.append("Abdullah")#Append add another element to the end of the list
print(friends)
# Sorting numbers list
num = [2,3,45,66,76,54,42,12,1,0]
num.sort()
print(num)
# Insert new element in list
friends.insert(2, "Musaab")  # Insert at index 2(index means numeric value of element)
print(friends)
# Remove element from list
friends.remove("Andriod")  # Remove element by value
print(friends)
# Pop element from list
friends.pop(2)  # Pop element by index 2 
print(friends)
# Tuples
# Tuples are immutable, meaning they cannot be changed after creation
a =(1,2,4.5, "Ashar", "Musaab", False)#Tuples can contain different data types
print(a)
no = (a.count("Ashar"))
print(no)  # Count occurrences of "Ashar" in the tuple

no = (a.index("Musaab"))  # Find the index of "Musaab" in the tuple
print(no)  # Print the index of "Musaab"

print(len(a))#Elemnt count in tuple