#ex1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))

#ex2
car1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car1["year"] = 2020
print(car1)

#ex3
car3 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car3["color"] = "red"
print(car3)

#ex4
car4 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car4.pop("model")
print(car4)

#ex5
car5 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car5.clear()
print(car5)