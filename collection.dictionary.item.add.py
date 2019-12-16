Add item to Dictionary
Note:
  -guidance @ https://www.w3schools.com/python/ref_dictionary_update.asp
Main Success Scenario:
  1.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

Alternatives:
  1a.Add another way 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "red"})

print(car)
