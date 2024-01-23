#ex 1
x = "Hello World"
print(len(x))

#ex 2
txt1 = "Hello World"
y = txt1[0]; 
print(y)

#ex 3
txt2 = "Hello World"
z = txt2[2:5]
print(z)

#ex 4
txt2 = " Hello World "
r = txt2.strip()
print(r)

#ex 5
txt5 = "Hello World"
txt5 = txt5.upper()
print(txt5)

#ex6
txt6 = "Hello World"
txt6 = txt6.lower()
print(txt6)

#ex7
txt7 = "Hello World"
txt7 = txt7.replace("H", "J")
print(txt7)

#ex8
age = 36
txt8 = "My name is John, and I am {}"
print(txt8.format(age))