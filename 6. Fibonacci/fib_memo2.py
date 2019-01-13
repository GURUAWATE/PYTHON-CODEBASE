message = """
                Here, we will use LRU cache. (Least Recently Used)
                This provides a simple way to add Memoization to your code.
           
                This is stored in 'functools' library, which we will import.
           
            from functools import lru_cache
            
                lru_cache is a Decorator,
                Decorators are used to extend the behaviour of latter function without explicitly modifying it.
                
                Syntax to use a Decorator: @decorator[(args)]
                
                To use this write @lru_cache() before our normal function.
                By default it will provide access to 128 recently used values,
                    to increse this, we will provide maxsize as an argument.
            
            @lru_cache(maxsize = 1000)
            def fibonacci(n):    
                
                if n == 1 or n == 2:
                    return 1
                else:
                    return (fibonacci(n - 1) + fibonacci(n - 2))
                    
                Now, Let's test this for n = 100
            
            for n in range(1, 101):
    
                print(n, " : ", fibonacci(n))
                
          """  
print(message)

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):    
                
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for n in range(1, 101):
    
    print(n, " : ", fibonacci(n))
    
print("\n\nNow try n = 10000, It will not let you down!\nBut Don't forgrt to Redirect the output to a file!!") 
print("\n\nBefore trying this, put all statements that print info inside comments.")
print("\n\nAnd then, Run your file like this:\n\t\t\t\t\tpython fib_memo2.py > fib_output.txt")