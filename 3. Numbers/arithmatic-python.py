a = 5
b = 15.00
c = 20.00 + 0j

print("\na = 5:")
print(a)
print(type(a))

print("\nb = 15.00:")
print(b)
print(type(b))

print("\nc = 20.00 + 0j:")
print(c)
print(type(c))

print("\n\nRule: Widen the narrower number, so that both are of same type:")

print("\nAddition:\n")
r = a + b
print("\nr = a + b (int + float):")
print(r)
print(type(r))

print("\nSubtraction:\n")
r = c - b
print("\nr = c - b (complex - float):")
print(r)
print(type(r))

print("\nMultiplication:\n")
r = a * c
print("\nr = a * c (int * complex):")
print(r)
print(type(r))

print("\nDivision:\n")
r = c / b
print("\nr = c / b (complex / float):")
print(r)
print(type(r))

r = 16 / 5
print("\nr = 16 / 5 (int / int):")
print(r)
print(type(r))

print("\nEven though we provided Both ints, the answer automatically got casted into float, Hence there's no need for specifying it explicitly.\n")


r = 20 / 5
print("\nr = 20 / 5 (int / int):")
print(r)
print(type(r))

print("\nEven if there is no remainder, the type of answer is still a float.\n")

r = 16 % 5
print("\nr = 16 % 5 (get remainder):")
print(r)
print(type(r))

r = 16 // 5
print("\nr = 16 // 5 (get quotient):")
print(r)
print(type(r))







