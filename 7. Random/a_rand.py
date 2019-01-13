message =  """  
                Random numbers are used for generating random numbers.
                This is used for bringing Unpredictability to your Game or for running Monte Carlo simulations.
                
                Random numbers are also used in Cryptography, But functions in Random module are not equipped for that kind of task,
                    If Cryptographically secure Pseudo Random numbers are required, then 'os.urandom()' or 'SystemRandom' should be used instead.
                 
                Now let's import the module & see what it has to offer.
                
                import random 
                
                print("Functions in 'random' module",  80*"---")
                print(dir(random))
                print(80*"---")
                help(random.random)
                
            """
print(message)
            
import random 
                
print("\nFunctions in 'random' module\n", 80*"---")
print(dir(random))
print(80*"---")
help(random.random)

message =  """  
                Now let's print random numbers in the from the interval 0 to 1.
                
                random ([n, m))
                The random function has default arguments as [0, 1)
                    
                    By default it generates random numbers from the interval 0 to 1.
                   
                    [0 Means random function can return 0.      
                    1) Means random function can not return 1.
                    
                    Values are chosen between 0.00 to 0.99, But not 1
                
                Loop for 10 times:
                
                for i in range(10)
                    print(random.random())
            """
print(message)

for i in range(10):
    print(random.random())
    
message =  """  
                Another feature of the random(), is that it represents 'Uniform Distribution'.
                    i.e. Probabilities of a number being chosen are equally spread out over the interval.
                
                But what if you wanted to get random number from different interval,
                    to do this, Lets write our own function.
                
                Let's pick interval 5 - 11
                
                1) Generate random() : [0, 1)
                
                    This will give you default interval of 0 - 1.
                
                2) Scale with the difference: [0, 6)
                
                    The difference of interval '5 - 11' is '6',
                    Now multiply the random() by the difference, '6'
                    
                    6 * random()
                    
                3) Set the Starting Value By Shifting: [5, 11)
                
                    This can be done directly by adding the 'Starting value' of the 'Interval'.
                    Starting value in this case is '5'.
                    
                    6 * random() + 5

                def my_random():
                        return (6 * random.random() + 5)
                
                Let's call this function 10 times.
                
                Values are chosen between 5.00 to 10.99, But not 11
            """
print(message)

def my_random():
    return (6 * random.random() + 5)
                
for i in range(10):
    print(my_random())