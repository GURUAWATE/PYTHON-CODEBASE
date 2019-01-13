message =   """
                List comprehension is a natural and easy way to describe a list in Mathematics. 
                    
                    e.g. 
                        S = { x^2 : x in {0 ... 9}} 
                        SE = {x | x in S and x even}
                        
                        You can write these in python as a Mathematician would on paper.
                        
                    Above lines are written in python as:
                        
                        S = [x**2 for x in range(10)]
                        
                            S will contain list of Squares of numbers 0 up to 9.
                            
                        SE = [x for x in S if x % 2 == 0]  
                        
                            SE will contain list of Even Numbers from the previous list S.
                            
                    TAKEWAY:
                             list_var = [expression <controls>]
                             
            """   
print(message)

S = [x**2 for x in range(10)]

print("\nValues in list S: ", S)

SE = [x for x in S if x % 2 == 0]

print("\nEven values in list S: ", SE)

message =   """
                More complex examples could be given:
                    
                    Generating list of lists.
                    
                    aspire = 'Guru loves to learn and he will live up to his name'
                    words = aspire.split()
                    
                        The split() with no arguments will tokenize the string 'aspire'.
                            as split has " " (space) as it's default argument.
                        
                        Now, words is a list of words from the string aspire.
                        
                    print("\String: ",aspire) 
                    print("\Tokenized String: ",words)
                    
                    
            """   
print(message)

aspire = 'Guru loves to learn and he will live up to his name'
words = aspire.split()

print("\nString: ",aspire) 
print("\n\nTokenized String: ",words)

message =   """
                Now, we will create new List that contains:
                    Uppercase and Lowercase forms of the words.
                
                UcLcLen = [[w.upper(), w.lower(), len(w)] for w in words]
                
                        Now lets print and see what we've got.
                        
                print(UcLcLen)        
                    
            """   
print(message)

UcLcLen = [[w.upper(), w.lower(), len(w)] for w in words]

print(UcLcLen)

message =   """
                Let's Iterate over it to make it more readable:

                for lol in UcLcLen:
                    print(lol)
                    
            """   
print(message)

for lol in UcLcLen:
    print(lol)