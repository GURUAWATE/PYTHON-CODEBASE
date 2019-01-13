message =   """
                
                def random_walk(n):
                
                    # Another way of Initializing
                    
                    x, y = 0, 0
                    
                    for i in range(n):
                        
                        # Now we will use tuple for change in direction dx, dy
                       
                            # There are 4 Possible Permutations of Directional Changes:
                                (dx, dy):
                                        (-1, 0) # Go Left   or
                                        (1, 0)  # Go Right  or  
                                        (0, -1) # Go Down   or
                                        (0, 1)  # Go Up
                                
                            # We will choose them using choice()  
                            
                        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                        
                        # You can aceess tuple elements directly, If no tuple variable is assigned.
                        
                        x += dx
                        y += dy

                    return(x, y)
                
                Now We will do same operations as previous program.
            """
print(message)

import random

def random_walk(n):
    
    x, y = 0, 0
    
    for i in range(n):
    
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        
        x += dx
        y += dy
        
    return(x, y)
    
for i in range(25):

        where_after_10_blocks = random_walk(10)
        
        far = abs(where_after_10_blocks[0]) + abs(where_after_10_blocks[1])
        
        print("Currently @ ", where_after_10_blocks, " Distance from home = ", far)