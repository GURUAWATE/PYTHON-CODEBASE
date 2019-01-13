def add(x, y):
    """Return the addition of values x & y"""
    return (x  + y)
            
def cm(feet = 0, inches = 0):
    """Convert feet & inches to centimeters"""
    feet_to_cm = feet * 12 * 2.54
    inches_to_cm = inches * 2.54
                
    return (feet_to_cm + inches_to_cm)

message = """
            def add(x, y):
                \"""docstring: <write your info here>\"""
                return (x  + y)
            
            def cm(feet = 0, inches = 0):
            
                \"""docstring: <write your info here>\""" 
                feet_to_cm = feet * 12 * 2.54
                inches_to_cm = inches * 2.54
                
                return (feet_to_cm + inches_to_cm)
                
            Docstrings:
                    
                Written in \"""___docstring___\"""
                
                Docstring, gives info about the function.
                It is a convention, Useful if followed,
                
                help(function_name) displays that function's docstring as:
                  
                >>> help(function.add)
                    Help on function add in module function:

                    add(x, y)
                        Return the addition of values x & y         
          """
print(message) 

print("\nprint(add(5, 15))")
print(add(5, 15))

print("\nprint(cm(feet = 5, inches = 4))")
print(cm(feet = 5, inches = 4))

print("\nprint(cm(feet = 5))")
print(cm(feet = 5))

print("\nprint(cm(inches = 4))")
print(cm(inches = 4))