# String methods in python
# String are immutable
'''
o len()
o upper()
o lower()
o rstrip()
o replace()
o split()
o capitalize()
o center()
o count()
o endswith()
o find()
o index()
'''

# a = "Harry"

# print(len(a))
# print(a.upper())
# print(a.lower())

# ========================

# a = "!!!Harry!!!!!!!"
# print(a.rstrip("!"))

# ========================

# a = "!!!Harry!!!!!!Harry"
# print(a.replace("Harry", "John"))

# =========================

# a = "!!! Harry!! !!!!!!!!!!!!!! Harry"
# print(a.split(" "))

# =========================

# blogHeading = "introduction to js"
# print(blogHeading.capitalize())

# ==========================

# str1 = "Welcome to the Console!!!"
# print(len(str1))
# print(str1.center(50))
# print(len(str1.center(50)))

# ============================

# a = "!!!Harry!!!!!!Harry"
# print(a.count("Harry"))

# =============================

# a = "!!!Harry!!!!!!Harry!!!"
# print(a.endswith("!!!"))

# str1 = "Welcome to the Console!!!"
# print(str1.endswith("to", 10, len(str1)))

# =================================

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))