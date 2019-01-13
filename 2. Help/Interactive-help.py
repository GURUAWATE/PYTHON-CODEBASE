message = """
          Python provides interactive help functions.
          First of them is directory function
          """
print(message)

print("\ndir()")
print(dir())

message = """
          dir() function lists out available objects.

          Major four of them are: builtins, doc, name, package.

          We can also check what each individual object has to provide.
          we just need to pass the object as an argument to the dir().
          """
print(message)

print("\ndir(__builtins__)")
print(dir(__builtins__))

message = """
          You can learn more about these functions using help() function, 
          You just need to pass object name as an argument to the help() function.
          """
print(message)

print("help(print)")
help(print)
print("help(pow)")
help(pow)
print("help(dir)")
help(dir)
print("help(help)")
help(help)

message = """
          You can serch for whatever object you want.
          \n\nUSE 'conda list' TO OBTAIN A LIST OF AVAILABLE MODULES.
          \nTHESE MODULES CAN BE IMPORTED USING 'import <module> [as <var>]' STATEMENT,
          
          And then use dir(<module>) to know about the functions provided in that module.
          
          But first we need to import the module we intend to use, and use '.' (dot) to access it's functions.
          
          For example, we will use :
                                    import math
                                    dir(math)
                                    help(math.log)
          """
print(message)
import math
print(dir(math))
help(math.log)



