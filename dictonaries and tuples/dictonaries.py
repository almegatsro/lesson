mydict = {}
mydict = {1: 'apple', 2: 'banana', 3: 'cherry'}
mydict = {'name': 'John', 1:[2, 4, 3]}
mydict = {'name': 'John', 'age': 23}
print(mydict["name"])
print(mydict['age'])
mydict['age'] = 25
print(mydict)
mydict["address"] = "Downtown"
print(mydict)
mydict.pop('age')
print(mydict)
print("address :", mydict.get("address"))
mydict.clear()
print(mydict)