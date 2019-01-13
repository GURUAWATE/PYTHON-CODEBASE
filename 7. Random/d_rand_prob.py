message =   """  
                Discrete Probability Distributions:
                
                Sometimes you don't want a random number to be chosen from an infinite number of possibilities.
                
                    e.g. What if you want to simulate the behaviour of a 'Six Sided Die'
                    
                    for this, you use randint(min, max) function.
                    
                        which gives a random integer from the interval [1, 6].
                        Notice [1, 6] Both have 'square brackets' [].
                        Meaning, 1 and 6 both have the possibility to get chosen.
                        
                Let's see help for this function.  
                
                import random
                
                print("Function randint(): ", 80*"-")
                help(random.randint)
                print(80*"-")
            """ 
print(message)

import random

print("\nFunction randint(): \n", 80*"-")
help(random.randint)
print(80*"-")

message =   """
  
                Now, let's roll 2 dice for 10 times:
                
                    We will create a tuple, 
                        then store the dice values &
                        then display them.
                    Repeat the process 10 times.    
                
                for i in range(1, 11):
                    tup = (random.randint(1, 6), random.randint(1, 6))
                    print(i, ":", tup)
            """ 
print(message)

for i in range(1, 11):
    tup = (random.randint(1, 6), random.randint(1, 6))
    print(i, ":", tup)