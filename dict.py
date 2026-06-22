 #clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary


#car = {
#"company1" : "TATA",
#"company2" : "BMW",
#"company3" : "Ford"
#}

#car = car.copy()
#x= car.get("company2")
#print(x)

#car.update({"company3" : "Audi"})
#car.pop("company1")
#print(car)

#car.update({"company3" : "Audi"})
#car.popitem("company1")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

vehicle = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = vehicle.keys()

print(x)


thisdic0t = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

y = thisdic0t.values()

print(y)
