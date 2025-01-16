# Tuple

tup = (1, 2, 76, 342, 32, "green")

print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(len(tup))


if 342 in tup:
    print("Yes 342 in present in this tuple")

tup2 = tup[1:4]
print(tup2)