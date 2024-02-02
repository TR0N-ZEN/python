array1 = []
tuple1 = ("1", "2", 3)

for element in {4, 2, 3}:
    # array1.append(element)
    print(element)

print(len({4, 2}))

x = 0
while (x < 5):
    print(x)
    x += 1

if (x == 4):
    x = 0
elif (x == 0):
    x = 4
else:
    x = 1

try:
    tuple1[1] = 0
except TypeError:
    print("landed in except because tuples do not support item assignment")
else:
    print("index esxists")
finally:
    print("finally")
