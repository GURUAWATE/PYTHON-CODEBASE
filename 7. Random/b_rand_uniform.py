message =  """  
                There is an easier way to get random numbers from any interval,
                Let's see what uniform function does and use it for this task.
                
                import random
                
                help(random.uniform)
                
            """
print(message)

import random
                
help(random.uniform)

message =  """  
                Now let's print random values from the interval 0 to 21,
                    And do this 10 times.
                    
                for i in range(10):
                    print(random.uniform(0, 21))
                
            """
print(message)

for i in range(10):
    print(random.uniform(0, 21))