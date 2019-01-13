message =   """
             Integers between 0 - 9
             
             even = set([0, 2, 4, 6, 8])
             odd = set([1, 3, 5, 7, 9])
             prime = set([2, 3, 5, 7])
             composite = set([4, 6, 8, 9])
             
            """
print(message)

even = set([0, 2, 4, 6, 8])
odd = set([1, 3, 5, 7, 9])
prime = set([2, 3, 5, 7])
composite = set([4, 6, 8, 9])

print("\nprint(even.union(odd))")
print(even.union(odd))

print("\nprint(even.intersection(odd))")
print(even.intersection(odd))

print("\nprint(even.union(prime))")
print(even.union(prime))

print("\nprint(odd.intersection(composite))")
print(odd.intersection(composite))

print("\nprint(2 in prime)")
print(2 in prime)

print("\nprint(1 in even)")
print(1 in even)  

print("\nprint(1 not in even)")
print(1 not in even)

print("\nprint(2 not in prime)")
print(2 not in prime)

print("\nNow explore more operations:\n\nprint(dir(set))")
print(dir(set))