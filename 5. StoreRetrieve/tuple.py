message = """
            List datatypes store data in order and sequence.
            Just as Lists, There is a smaller and faster alternative: Tuples
            There are two ways to make a Tuple.
            
            tup1 = (1,) # Adding a trailing comma is necessesary if the tuple contains a single element.
            
            tup2 = 1,
            
            primes_tuple = (2, 3, 5, 7)
            
            print(tup1)
            print("Type: ", type(tup1))
            print(tup2)
            print("Type: ", type(tup2))
            print(primes_tuple)
            print("Type: ", type(primes_tuple))
            
          """  
print(message)

tup1 = (1,) 
tup2 = 1,
primes_tuple = (2, 3, 5, 7)
            
print(tup1)
print("Type: ", type(tup1))
print(tup2)
print("Type: ", type(tup2))
print(primes_tuple)
print("Type: ", type(primes_tuple))

message = """
            List takes more size, because it contains more operations/functions.
                you can checkout available functions for both using dir().
            
            print("Tuple functions:")    
            print(dir(tuple)) 
            print(80*"-")
            print("List functions:") 
            print(dir(list))
            
            primes_list = [2, 3, 5, 7]
            
            print("Now let's compare size of both, List And Tuple containing similar elements and length")
            
            print("List: ", primes_list)
            print("Tuple: ", primes_tuple)
            
            import sys
            
            print("Size of List: ", sys.getsizeof(primes_list))
            print("Size of Tuple: ", sys.getsizeof(primes_tuple))
            
          """  
print(message)

print("\nTuple functions:\n")    
print(dir(tuple)) 
print(160*"-")
print("\nList functions:\n") 
print(dir(list))
            
primes_list = [2, 3, 5, 7]
            
print("\nNow let's compare size of both, List And Tuple containing similar elements and length\n")

print("\n\nList: ", primes_list)
print("\n\nTuple: ", primes_tuple)
            
import sys
            
print("\nSize of List: ", sys.getsizeof(primes_list))
print("\nSize of Tuple: ", sys.getsizeof(primes_tuple))


message = """
            
            Lists:  Allow operation like:
            
                    Add Data,
                    Remove Data,
                    Change Data
                    
            Tuples: Can not be changed, They are 'Immutable'.
                    This help python to make significant optimization.
            
            
            Tuples can be created faster than lists,
                We will check this by creating 1M list & 1M tuples and compare the operation time.
            
            import timeit
            
            list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000)
            tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000)
            
            print("Time taken to create a Million Lists: ", list_test)
            print("Time taken to create a Million Tuples: ", tuple_test) 
          """  
print(message)

import timeit
            
list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000)
            
print("\n\nTime taken to create a Million Lists: ", list_test)
print("\n\nTime taken to create a Million Tuples: ", tuple_test)

message = """
            
            Accessing tuples:
            
            info = (21, "Male", "Solapur")
            
            age = info[0]
            sex = info[1]
            loc = info[2]
            
            print("Age: ", age, "Sex: ", sex, "Location: ",loc)
            
          """  
print(message)

info = (21, "Male", "Solapur")
            
age = info[0]
sex = info[1]
loc = info[2]
            
print("\nAge: ", age, "\nSex: ", sex, "\nLocation: ",loc)

message = """
            
            But tuples provide a faster alternative:
           
            a, s, l = info
            
            This will unpack the tuple, and assign values to variables.
                
                But be careful though,
                providing less or more variables than the values contained by a tuple, will give you an ValueError.
                
                Hence the number of varibles should be equal to the number of values contained in tuple. 
            
            print("Age: ", a, "Sex: ", s, "Location: ",l)
            
          """  
print(message)

a, s, l = info

print("\nAge: ", a, "\nSex: ", s, "\nLocation: ",l)