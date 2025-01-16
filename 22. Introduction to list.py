# Introduction to list

# marks = [3, 5, 6]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# ======================================

marks = [3, 5, 6, "Harry", True, 3, 7, 6, 8, 9]
# print(marks)
# print(marks[3])
# print(marks[4])

# =========================================
# Negative index

# print(marks[-3]) 
# print(marks[len(marks) - 3])

# ========================================

# if 7 in marks:
#     print("7 is there")
# else:
#     print("NO")


if "Harry" in marks:
    print("Yes")
else:
    print("No")

# ========================================
# slicing

# print(marks)
# print(marks[1: 4])
# print(marks[1 : -1])
# print(marks[1:8:3])

# =======================================

lst = [i * i for i in range(10)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)