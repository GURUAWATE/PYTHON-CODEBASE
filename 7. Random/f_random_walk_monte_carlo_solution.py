message =   """   
                Puzzle Question:
                    
                    What is the longest random walk you can take,
                        so that on average you will end up 4 blocks or fewer from home. ?
                Answer:
                        Here, Instead of solving the problem mathematically,
                            We will conduct thousands of trials,
                                to compute the percentage of random walks that end up in 4 or fewer blocks away from the origin.
                
                number_of_walks = 10000
                
                # We will take total 10000 random walks, For each, From 1 to 30 Blocks
                
                for blocks_to_walk in range(1, 31):
               
                    desired_walks = 0
                    # Maintain a counter 
                    
                    for i in range(number_of_walks):
        
                        (x, y) = random_walk(blocks_to_walk)
        
                        distance = abs(x) + abs(y)
        
                        if distance <= 4:
                            desired_walks += 1
                        # Update the counter
                        
                    percet_desired_walks = 100 * (float(desired_walks) / number_of_walks)
                    
                    # Calculate & Print % for each Walk
                    
                    print("Blocks walked = ", blocks_to_walk, "With % of Desired walks = ", percet_desired_walks)
                               
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

number_of_walks = 10000

for blocks_to_walk in range(1, 31):

    desired_walks = 0
    
    for i in range(number_of_walks):
        
        (x, y) = random_walk(blocks_to_walk)
        
        distance = abs(x) + abs(y)
        
        if distance <= 4:
            desired_walks += 1
            
    percet_desired_walks = 100 * (float(desired_walks) / number_of_walks)
    
    print("Blocks walked = ", blocks_to_walk, "With % of Desired walks = ", percet_desired_walks)


message =   """   
            
                The longest walk,
                    with the greater than 50% chance of desired outcome,
                    is of 22 blocks.(When tested for blocks ranging from 1 to 30)
            """
print(message)   
        