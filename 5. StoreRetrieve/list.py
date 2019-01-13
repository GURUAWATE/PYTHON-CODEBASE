message = """
            List datatypes store data in order and sequence.
            There are two ways to make a list.
            
            list1 = list()
            list2 = []
            
            You can also intialize values while declaring, 
                & add data at the end of the list using append(element) function
                
            primes = [2, 3, 5, 7]
            
            print(primes)
          """  
print(message)  
        
primes = [2, 3, 5, 7]
            
print(primes)

message = """
            primes.append(11)
            primes.append(13)
            primes.append(17)
            primes.append(19)
            
            print(primes)
          """  
print(message) 

primes.append(11)
primes.append(13)
primes.append(17)
primes.append(19)
            
print(primes)

message = """
            for elements in primes:
                print(elements)
          """  
print(message) 

for elements in primes:
    print(elements)

message = """
            List also allows wrap around, but for only only once.
            
            wrap = 0 - len(primes)
            i = 0
            
            while i >= wrap:
                print(primes[i])
                i -= 1
          """  
print(message)

wrap = 0 - len(primes)
i = -1
            
while i >= wrap:
    print(primes[i])
    i -= 1
    
print("\nNow it will give Index error, If you tried to wrap-around again,\nThis is not allowed from index: ", wrap -1)

message = """
            List allows slicing, meaning displaying a part of the list.
            
            This is done with list_var[start_index : (stop_index + 1)]
            
            slice [2 : 6], will display values from index --> 2 upto index --> 5
            
            print(primes[2 : 6])
          """  
print(message)

print(primes[2 : 6])

message = """
            Lists can contain multiple datatype, sub-lists, and duplicate values.
            
            example = []
            
            example.append('Guru')
            example.append(14)
            example.append(19.95)
            example.append([14, 11, 1995])
            example.append('Guru')
            
            print(example)
          """  
print(message)

example = []
            
example.append('Guru')
example.append(14)
example.append(19.95)
example.append([14, 11, 1995])
example.append('Guru')
            
print(example)

message = """
            Lists can be combined using '+' operator.
            
            combine = primes + example
           
            print(combine)
          """  
print(message)

combine = primes + example
           
print(combine)

message = """
            Lists contain many such operations, 
            check them out using help() & dir().
            
            help(list.reverse)
            print(dir(list))
            
          """  
print(message)

help(list.reverse)
print(dir(list))