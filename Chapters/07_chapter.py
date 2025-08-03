# Loops
#for loop
for i in range(1, 6):
    print(i)
#Same task can take much time
print(1)
print(2)
print(3)
print(4)
print(5)
#while loop
b =1
while(b<6):
    print(b)
    b +=1

#Print list using while
l =[1, "Usman", "Ashar", "Abdullah", 3.456]

i=0
while (i<len(l)):
    print(l[i])
    i+=1
#Print table using for
for i in range(0 , 102, 4):
    print(i)

#Tuples, string and list printing
l = [34, 56, 6.7, 9]
for i in l:
    print(i)

t =(343,13,3243,4343,45)
for i in t:
    print(i)

s = "Musaab"
for i in s:
    print(i)

#List with for and else

l =[3,45,56.5,"Musaab"]
for items in l:
    print(items)
else:
    print("Done")

#Using break statement(this exists the loop)
for i in range(100):
    if(i == 51):
        break
    print(i)

#Using continue statement(this just skips the particular number or string)
for i in range(100):
    if(i == 51):
        continue
    print(i)

#Use pass(This skips the pass on loop giving user opportunity to use it when he wants)
for i in range(634):
    pass

i = 0
while (i < 45):
    print(i)
    i += 1