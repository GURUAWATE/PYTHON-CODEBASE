message =  """  
                So why did we bother to write our own function ?,
                    
                    We did this to highlight an important fact:
                    The random() function can be used to build customized random number generators.
                    
                random() & uniform() are both uniform distributions.
                    
                    But there are other distributions as well,
                    where some group of numbers are more likely Tobe chosen than others.
                    
                    viz. Normal Distributions (a.k.a. The Bell Curve).
                    
                The Normal Distribution can be completely described by just two numbers:
                    
                    Mean: Represented by Mu ( μ )
                            
                            It's the average, it's where the bell curve peaks.
                    
                    Standard Deviation: Represented by Sigma( σ )
                            
                            It describes how wide or narrow the curve is.
                
                To generate random numbers from normal distribution,
                
                    we use normalvariate(μ, σ) function.
                    
                let's see the help for this function:
                
                import random
                
                print("NormalVariate: ", 80*"-")
                help(random.normalvariate)
                print(80*"-")
            """ 
print(message)

import random

print("\nNormalVariate: \n\n", 80*"-")
help(random.normalvariate)
print(80*"-")

message =   """  

                Let's generate 20 random numbers from a 'Bell curve'
                    with μ = 0 & σ = 1.
                
                for i in range(20):
                    print(random.normalvariate(0, 1))
                    
                Notice How the numbers are bunched around the mean 0.    
            """ 
print(message)

for i in range(20):
    print(random.normalvariate(0, 1))
    

message =   """ 
 
                now with μ = 0 & σ = 9.
                
                for i in range(20):
                    print(random.normalvariate(0, 9))
                    
                Notice that the numbers are now more widely spread out.    
            """ 
print(message)

for i in range(20):
    print(random.normalvariate(0, 9)) 

message =   """ 
 
                now with μ = 0 & σ = 0.2
                
                for i in range(20):
                    print(random.normalvariate(0, 0.2))
                    
                If you make 'Standard Deviation' small, the numbers will be tightly grouped.
                
            """ 
print(message)

for i in range(20):
    print(random.normalvariate(0, 0.2)) 

message =   """ 
 
                now with μ = 5 & σ = 0.2
                
                for i in range(20):
                    print(random.normalvariate(5, 0.2))
                    
                Notice that the numbers are now bunched around the mean 5.
                
            """ 
print(message)

for i in range(20):
    print(random.normalvariate(5, 0.2))       