message = """
            Fibonacci series, It goes like this: 1, 1, 2, 3, 5, 8, ....
                First two terms are 1 & 1
                Third term is sum of previous two terms i.e. 1 + 1 = 2
                Fourth term is sum of previous two terms i.e. 1 + 2 = 3
                Fifth term is sum of previous two terms i.e. 2 + 3 = 5
                    And so on.........
            
            One way to solve this problem is to use recursion, i.e. function calling itself.
                
            def fibonacci(n):    
                
                if n == 1 or n == 2:
                    return 1
                else:
                    return (fibonacci(n - 1) + fibonacci(n - 2))
            
            Now, Let's print series upto 10:
            
            for n in range(1, 11):
    
                print(n, " : ", fibonacci(n))
                        
          """  
print(message)

def fibonacci(n):    
                
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for n in range(1, 11):
    
    print(n, " : ", fibonacci(n))
    
message = """
            
            
            This is tolerable only for a small sequences, But it gets annoying over large sequences.
                we will solve this problem with 'caching' in next example.
           
                # Trust me, You don't wanna put a number larger than 35.
                # You don't want your call stack to be exhausted, If you're curious then try it out.
                
                
                
                
                What happens when you call fibonacci():
                let's illustrate it with n = 5:
                
                fibonacci(5) = fibonacci(4) + fibonacci(3)
                               
                    fibonacci(4) = fibonacci(3) + fibonacci(2)
                    
                    fibonacci(3) = fibonacci(2) + fibonacci(1)
                        
                            ............. Our computer is calculating the same thing over and over again....
                            
                To make this process faster we will use caching (Memoization),
                    Refer files: fib_memo1.py & fib_memo2.py
          """  
print(message)