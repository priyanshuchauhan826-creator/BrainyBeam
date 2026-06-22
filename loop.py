#print 10 number usin loop

for x in range(11):
    print(x)


#print 10 nuber using wile loop
i=1
while i < 11:
    print(i)
    i +=1
    
  

for i in range(1,6):
    print(i *"*")


for j in range(6,1,-1):
    print(j *"*")

start=int(input("Enter number of rows:"))
end=int(input("Enter number of rows:"))
for i in range(start,end+1):
    print(i *"*")