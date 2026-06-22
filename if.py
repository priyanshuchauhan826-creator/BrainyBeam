#if,elif,else

a=10
b=10
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("zero")


#nested if

grade = 10
if grade >=90:
    print("A")
if grade >=80:
    print("B")
else:
    print("Fail")


#match 

month = 5
match month:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("April")
    case 5:
        print("May")
        