#1 Program to create a list of fruits and print them
fruits = []

f1 = input("Enter the first fruit: ")
fruits.append(f1)
f2 = input("Enter the second fruit: ")
fruits.append(f2)
f3 = input("Enter the third fruit: ")
fruits.append(f3)
f4 = input("Enter the fourth fruit: ")
fruits.append(f4)
f5 = input("Enter the fifth fruit: ")
fruits.append(f5)
f6 = input("Enter the sixth fruit:")
fruits.append(f6)
f7 = input("Enter the seventh fruit: ")
fruits.append(f7)

print(fruits)

#2 
studentmarks = []

m1 = input("Enter the first students marks: ")
studentmarks.append(m1)
m2 = input("Enter the second students marks: ")
studentmarks.append(m2)
m3 = input("Enter the third students marks: ")
studentmarks.append(m3)
m4 = input("Enter the fourth students marks: ")
studentmarks.append(m4)

studentmarks.sort() # Sort the marks in ascending order
print(studentmarks)

#3
#Sum 
sum1 = [32,43,44,56]

print(sum(sum1))
#4 
# Count Number in tuple
tup = (1, 9, 3, 4, 0, 6, 0, 8, 9, 0)

print(tup.count(0))  # Count occurrences of 0 in the tuple