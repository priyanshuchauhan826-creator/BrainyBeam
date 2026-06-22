color={"red","blue","green","orange","purple"}
color.add("black")
print("black" in color)
print("violet" not in color)
color.remove("black")
print(color)
del color


set1={"apple","banana","orange","mango"}
set2={1,2,3,4,5}
set3 = set1 | set2
print(set3)



x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)


a={"google","microsoft","apple"}
b={"mango","apple","orange"}
c=a.intersection(b)
print(c)


a={"google","microsoft","apple"}
b={"mango","apple","orange"}
c = a & b
print(c)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)