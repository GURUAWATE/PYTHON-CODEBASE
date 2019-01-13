message = """
            Memoization: 
                        Cache (store) the results of recent function calls,
                        So that future calls do not have to repeat the work that has already been done.
                        
            Memoization can be implemented:
            
                1. Explicitly.
                2. By Using a built-in python tool.
            
            1. Explicit method
            
            Create a dictionary that stores results of function calls.
            fibonacci_cache = {}
            
            Rewrite the fibonacci() to make use of cached values:
            def fibonacci(n):    
                
                # If we have the cached value then simply return it:
                if n in fibonacci_cache:
                    return fibonacci_cache[n]
                
                # Else calculate the value and cache it for later use:
                if n == 1 or n == 2:
                    value = 1
                else:
                    value = (fibonacci(n - 1) + fibonacci(n - 2))
                
                fibonacci_cache[n] = value
                return value
                
                Now if you even give n = 1000, This process will not let you down.
                
                For the sake of reading this output, we will use n = 50 (Feel free to try any number)
                
                for n in range(1, 51):
    
                    print(n, " : ", fibonacci(n))
                    
                I suggest directing your output to a text file, if you plan on using n = 10K as:
                    python fib_memo.py > fib_output.txt (The text file will be larger than 10MB)
            
          """  
print(message)

fibonacci_cache = {}

def fibonacci(n):   
 
    if n in fibonacci_cache:
        return fibonacci_cache[n] 
        
    if n == 1 or n == 2:
        value = 1
    else:
        value = (fibonacci(n - 1) + fibonacci(n - 2))
                
    fibonacci_cache[n] = value
    return value

for n in range(1, 51):
    
    print(n, " : ", fibonacci(n))

print("\nNow checkout fib_memo2.py, for 2nd method for Memoization\n")  
