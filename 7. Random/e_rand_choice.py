message =   """  
                Sometimes you may want a random selection from a Sequence, which may be of any type.
                    The sequence may be of any format viz. list, tuple etc.
                    
                In such situations, we will use choice(<sequence>)
                
                Let's see help for this function.
            """ 
print(message)

import random

print("\nFunction choice(): \n", 80*"-")
help(random.choice)
print(80*"-")

message =   """  
                Now, Let's play Rock, Paper, Scissors for 10 times.
                
                hand = ('Rock', 'Paper', 'Scissors')
                
                for i in range(1, 11):
                    print(i, ": ", random.choice(hand))
            """ 
print(message)

hand = ('Rock', 'Paper', 'Scissors')
                
for i in range(1, 11):
    print(i, ": ", random.choice(hand))