# ex1
# def generate_ints(N):
#    for i in range(1, N+1):
#         yield i**2
#         i += 1

# N = int(input())

# square = generate_ints(N)
# for i in range(1, N+1):
#     print(next(square))

# try:
#     print(next(square))
# except StopIteration:
#     pass

# def even_numbers(n):
#     for i in range(n+1):
#         if i % 2 == 0:
#             yield i
#         i += 1

# try:
#         n = int(input())

#         even_gen = even_numbers(n)
#         even_list = list(even_gen)
#         print(",".join(map(str, even_list)))

# except ValueError:
#         print("Invalid input")

# def numbers(n):
#     for i in range(0,n+1):
#         if i % 3 == 0 or i % 4 == 0:
#             yield i
#         i += 1

# try:
#         n = int(input())

#         even_gen = numbers(n)
#         even_list = list(even_gen)
#         print(" ".join(map(str, even_list)))

# except ValueError:
#         print("Invalid input")

#ex4
# import math
# def squares(a, b):
#     for i in range(a, b+1):
#         yield math.pow(i, 2)
#         i += 1

# a = int(input())
# b = int(input())

# for i in squares(a, b):
#     print(i)

#ex5
# def desc(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n = int(input())

# for i in desc(n):
#     print(i)
