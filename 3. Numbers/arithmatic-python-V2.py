a = 5
b = 10L
c = 15.00
d = 20.00 + 0j

print "\na = 5:"
print a
print type(a)

print "\nb = 10L:"
print b
print type(b)

print "\nc = 15.00:"
print c
print type(c)

print "\nd = 20.00 + 0j:"
print d
print type(d)

print "\n\nRule: Widen the narrower number, so that both are of same type:"

print "\nAddition:\n"
r = a + b
print "\nr = a + b (int + long):"
print r
print type(r)

print "\nSubtraction:\n"
r = c - b
print "\nr = c - b (float - long):"
print r
print type(r)

print "\nMultiplication:\n"
r = a * c
print "\nr = a * c (int * float):"
print r
print type(r)

print "\nDivision:\n"
r = d / c
print "\nr = d / c (complex / float):"
print r
print type(r)

r = 16 / 5
print "\nr = 16 / 5 (int / int (both whole)):"
print r
print type(r)

r = 16 % 5
print "\nr = 16 % 5 (get remainder):"
print r
print type(r)

r = float(16) / 5
print "\nr = float(16) / 5 (float / int):"
print r
print type(r)

r = 16 / float(5)
print "\nr = 16 / float(5) (int / float):"
print r
print type(r)






