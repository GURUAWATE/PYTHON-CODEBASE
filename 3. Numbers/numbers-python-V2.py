message = """\n\nThere are 4 types of numbers in  python-2 & 3 types of numbers in python-3
              
              Now we will see python-2 numbers which are of 4 types, 
              
              namely: int, long, float & complex.
              
              ints & longs are whole numbers and floats are real numbers.
              
              where complex has combination of real & imaginary numbers.             
          """
print message

a = 10

print "\nPrint function comes with built-in '\\n' character"

print a

print "print function does not need parenthesis () in python 2\n\nYou can also use type(var) to know the type of variable"

print type(a)

b = 43.12
print b
print type(b)

print "\nYou can also use sys to know max value of types, But first you need to import sys\n"

import sys

print "int: " 
print -sys.maxint - 1
print sys.maxint
print "\nfloat: "  
print -sys.float_info.max -1
print sys.float_info.max
print "\nlong type (maxint + 1): \n" 
print sys.maxint + 1 
print type(sys.maxint + 1)

print "\nYou don't have to worry about upper-lower bounds of a type,\nBecause python will automatically convert it for you"

another_comment = """\nComplex numbers are usually represented as z = 46 + 5i 

                     But python uses letter 'j' instead as z = 46 + 5j
                  """
print another_comment 

z = 46 + 5j
print z
print type(z)
print "\nprint real part only via z.real"
print z.real   
print "\nprint imaginary part only via z.imag"
print z.imag              
