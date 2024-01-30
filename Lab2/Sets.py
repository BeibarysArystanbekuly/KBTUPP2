#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#ex2
fruits1 = {"apple", "banana", "cherry"}
fruits1.add("orange")
print(fruits1)

#ex3
fruits2 = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits2.update(more_fruits)
print(fruits2)

#ex4
fruits3 = {"apple", "banana", "cherry"}
fruits3.remove("banana")
print(fruits3)

#ex5
fruits4 = {"apple", "banana", "cherry"}
fruits4.discard("banana")
print(fruits4)