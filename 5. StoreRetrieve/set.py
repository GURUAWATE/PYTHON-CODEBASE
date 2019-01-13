message = """
            example = set()
            print(dir(example))
            help(example.add)
          """  
print(message)  
        
example = set()
print(dir(example))
help(example.add)

message = """
            example.add(False)
            example.add(3.14)
            example.add("No Order & Any Type")
            example.add(32)
            
            print(example)
          """  
print(message) 

example.add(False)
example.add(3.14)
example.add("No Order & Any Type")
example.add(32)
            
print(example)

message = """
            Set contains Unique values,See if it Ignores Duplicate Values:
            
            example.add(32)
            example.add(False)
     
            print(example)
          """  
print(message) 

example.add(32)
example.add(False)

print(example)

print("\nNumber of elements in Set: ", len(example))

message = """
            Removing an element:
            
            remove(element): This gives error if we try to remove a non-member element.
            
            discard(element): Removes element if exists & does nothing if element is a non-member.
     
            example.discard(54)
            example.discard(32)
            
            print("Number of elements in Set: ", len(example))
            print(example)
            
          """  
print(message)

example.discard(54)
example.discard(32)
            
print("\nNumber of elements in Set: ", len(example))
print(example)

print("\nexample1 = set([14, 'I Love Guru', 88.88])")
example1 = set([14, 'I Love Guru', 88.88])
print("\nNumber of elements in Set: ", len(example1))
print("print(example1)")
print(example1)

print("\nexample1.clear()")
example1.clear()
print("\nNumber of elements in Set: ", len(example1)) 
print("print(example1)")
print(example1)