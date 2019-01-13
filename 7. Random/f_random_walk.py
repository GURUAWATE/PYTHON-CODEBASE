message =   """
                
                Random walk:
                            your directions are chosen at random at each step.
                            at the end we will use 'Monte Carlo' simulation to solve this puzzle.
                
                Suppose you live in a city where the streets are arranged in a perfect 'Grid'.
                    You decide to go for walk, at each 'Intersection' you choose your next direction randomly.
                    Your choices of direction are: 'North', 'South', 'East' & 'West'.
                        Backtracking is permitted.
                    
                    When you're finished, you check to see how far you are from where you began(home).
                    
                def random_walk(n):
                
                    # Let the initial coordinates be (0, 0)
                    x = 0
                    y = 0
                    
                    for i in range(n):
                        
                        # Now take a walk of 'n' blocks, Turning at each block
                    
                        # Choose direction randomly
                        turn = random.choice(('N', 'S', 'E', 'W'))
                        
                        if turn == 'N':     # Go Up
                            y = y + 1
                        elif turn == 'S':   # Go Down
                            y = y - 1
                        elif turn == 'E':   # Go Right
                            x = x + 1
                        else:               # Go Left
                            x = x - 1
        
                    return(x, y) # Return the coordinates after walking 'n' blocks 
                
                Now Let's Take 25 Random Walks of 10 Blocks each,
                    i.e. Travel for total 250 Blocks 
                
                for i in range(25):

                    where_after_10_blocks = random_walk(10)
        
                    far = abs(where_after_10_blocks[0]) + abs(where_after_10_blocks[1])
                    
                    # far = abs(x) + abs(y)
                    
                    # As we started from (0, 0), 
                    
                        # The distance in blocks, will be the sum of absolute values of x, y.
                        # Sign will tell you the distance with direction,
                        # But we're interested in knowing only the distance, So we take the absolute values
                        
                    # For e.g. 
                                1) x = -10, y = 5
                                2) x = 10, y = 5
                                
                            In both the cases, you are 15 units away from the 'Origin'
        
                    print("Currently @ ", where_after_10_blocks, " Distance from home = ", far)
            """
print(message)

import random

def random_walk(n):
    """Return the coordinates after 'n' blockes of random walk."""
    
    x = 0
    y = 0
    
    for i in range(n):
        turn = random.choice(('N', 'S', 'E', 'W'))
        
        if turn == 'N':
            y = y + 1
        elif turn == 'S':
            y = y - 1
        elif turn == 'E':
            x = x + 1
        else:
            x = x - 1
        
    return(x, y)
    
for i in range(25):

        where_after_10_blocks = random_walk(10)
        
        far = abs(where_after_10_blocks[0]) + abs(where_after_10_blocks[1])
        
        print("Currently @ ", where_after_10_blocks, " Distance from home = ", far)