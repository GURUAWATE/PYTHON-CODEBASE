message = """\n\nThere are 3 types of numbers in python-3
              
              Now we will see python-3 numbers, 
              
              namely: int, float & complex. (there is no need for long)
              
              ints are whole numbers and floats are real numbers.
              
              where complex has combination of real & imaginary numbers.
                
              print() requires parenthesis '()'
          """
print(message)

a = 10

print(a)

print ("\nYou can also use type(var) to know the type of variable")

print(type(a))

b = 43.12
print(b)
print(type(b))


another_comment = """\nNotice that int and flot here are defined as classes.
                    
                     There are no size limits in python 3, 
                     Provided that your computer is able to handle that kind of huge number..

                     Complex numbers are usually represented as z = 46 + 5i 

                     But python uses letter 'j' instead as z = 46 + 5j
                  """
print(another_comment) 

z = 46 + 5j
print(z)
print(type(z))

print("\nPrint real part only via z.real:\n")
print(z.real)  
print("\nPrint imaginary part only via z.imag:\n")
print(z.imag)        
