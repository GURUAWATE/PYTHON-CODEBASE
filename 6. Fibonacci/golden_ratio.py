message = """
            Golden Ratio:
            
                If we took  Ratio of 'Next : Current' values,
                    We would get the rusult = 1.618033....
                
                    If we keep on taking the ratios, we will keep getting the same results forever.

            Now let's print these ratios:
            
            for n in range(1, 100):
                print(fibonacci(n + 1) / fibonacci(n))            
          """  
print(message)

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):    
                
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for n in range(1, 100):
    print(fibonacci(n + 1) / fibonacci(n))