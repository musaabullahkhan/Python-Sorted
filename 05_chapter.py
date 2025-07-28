# 1, Dictionary Example
marks = {
    "Musaab": 85,
    "Ashar": 90,
    "Abdullah": 78,
    "Usman": 29
}
print(marks, type(marks))
#  if you type 0 in a dictionary it will not be considered as a key, example:
# print(marks[0])
#But if you type key instead of 0 it will print the corresponding value, example:
print(marks["Musaab"])  # Output: 85

# 2, Dictionary methods
# Method 1
print(marks.items()) 
# Method 2
print(marks.keys()) #This will print all the keys 
# Method 3
print(marks.values()) #This will print all the values
# Method 4
marks.update({"Musaab": 86, "Ahsan": 99}) # This will change the original value of the key "Musaab" from 85 to 86 and if "Ahsan" is not present, it will add it with value 99
print(marks)
# Method 5
print(marks.get("Musaab"))  # This will return the value of the key "Musaab"
# Sets
s = {1 ,2 ,4 ,3 , 4, 4 ,5, 7, "Musaab"} #No repition allowed in sets(It is unordered)
print(s, type(s))  
s.add("Ashar")  # Adding a new element to the set
print(s)
# Remove item
s.remove(1)  # This will remove the element 1 from the set
print(s)
# Union and Intersection
s1 = {1, 2, 7, 6}
s2 = {3, 4, 47, 6}

print(s1.union(s2)) # Union of two sets
print(s1.intersection(s2))  # Intersection of two sets