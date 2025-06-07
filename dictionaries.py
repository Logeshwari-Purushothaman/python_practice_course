#Dictionaries
#key-value pairs are dictionary
#they are called object in java

car = {
    "brand" : "Tesla",
    "model" : "Model_3_P",
    "year" : 2024
}

car2 = dict(brand = "Tesla",model ="model_2")

print(car)
print(car2)
print(type(car))

print(isinstance(car,dict))
print(len(car))

#how to access values in inside dictionaries
print("\n")
print(car["brand"])
print(car.get("model"))

#list all keys in dictionary
print(car.keys())
#list all values in dictionary
print(car.values())

#list all key value pairs as dictionaries
print(car.items())

#how to verify a key exists
print("model" in car)
print("price" in car)

#how to change values in key
car["brand"] = "Nio"
print(car)

car.update({"price" : 10000})
print(car)

#how to remove items in dictionary
print(car.pop("price"))
print(car)

car["Ev"] = "yes"
print(car)
#popitem will remove and return both key and value together as a tuple
print(car.popitem())
print(car)

car["Ev"] = "yes"
#to delete a key value pair
del car["Ev"]
print(car)

#to empty the dictionary without deleting the whole dict

car2.clear()
print(car2)

#to delete the whole dict
del car2


#copy dictionary- wrong way
#below is the wrong way to do it, it will only create a reference
# car2 = car
# print("\n")
# print(car2)
# print(car)

#copy dictionary - right way
car2= car.copy()
car2["Ev"] = "No"
print("Good Copy")
print(car)
print(car2)

#copy dictionary - right way another way
car3 = dict(car)
print("good way 2")
print(car3)

#nested dictionaries
member1 = {
    "name" : "Page",
    "instrument" : "model"
}
member2 = {
    "name" : "Page",
    "instrument" : "model"
}
band = {
    "member1" : member1,
    "member2" : member2
}

print("---------")
print(band)
print(band["member2"]["instrument"])

#keys should be unique inside a dict