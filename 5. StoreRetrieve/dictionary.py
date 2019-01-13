message = """
            Dictionary is a map of keys and their associated values.
            They can be made as:
            
            dict_var = {key : value, key1 : value1, ........, keyN : valueN}
            
            And as always type is not the issue, storing multiple datatypes is allowed.
            
            We can also use, dict() constructor to make a dictionary.
            
            dict_var = dict(key = value, key1 = value1, ....., keyN = valueN)
            
            
            
            Example:
            
            dict1 = dict(name = "Gururaj Awate", age = 21)
            
            dict1["location"] = "Solapur"
            
          """  
print(message)  
        
dict1 = dict(name = "Gururaj Awate", age = 21)

dict1["location"] = "Solapur"

message = """
            Dictionary is sensitive to keys,
            It will give you 'KeyError' if you try to read a non-existing key.
            
            To avoid this, we use Error - Handling.
            
                try:
                    <statements likely to cause error>
                except <error-type>: 
                    <statements to handle the error>
                    
            Example:
            
            try:
                print(dict1["sex"])
            except KeyError: 
                print("key "sex", does not appear in the dictionary, Please check the key to access the value.")
                print("Here's the dictionary for your reference: ", dict1)
          """  
print(message)
            
try:
    print(dict1["sex"])
except KeyError: 
    print("\nkey \"sex\", does not appear in the dictionary, Please check the key to access the value.")
    print("\nHere's the dictionary for your reference: ", dict1)

print("\n\nExecution doesn't interrupt due to error handling.\n\nprint(dict1[\"name\"])\n")     
print(dict1["name"])

message = """
            We avoid the hassle, of writing
            
                try:
                    <statements likely to cause error>
                except <error-type>: 
                    <statements to handle the error>
                    
                With the help of Dictionary functions.    
                    
            Dictionary has a function get(),
            
            dict_var.get("key", <default value if key is not present>)
            
            \n\n\n
            
            Example:
            
            print(dict1.get("sex", "Key Doesn't Exist"))
            
          """  
print(message)


print(dict1.get("sex", "Key Doesn't Exist"))

message = """
            Now, let's add key --> sex, & check agin.
            
            dict1["sex"] = "Male"
            
            print(dict1.get("name", "Key Doesn't Exist"))
            print(dict1.get("age", "Key Doesn't Exist"))
            print(dict1.get("sex", "Key Doesn't Exist"))
            print(dict1.get("location", "Key Doesn't Exist"))
          """  
print(message)

dict1["sex"] = "Male"
            
print(dict1.get("name", "Key Doesn't Exist"))
print(dict1.get("age", "Key Doesn't Exist"))
print(dict1.get("sex", "Key Doesn't Exist"))
print(dict1.get("location", "Key Doesn't Exist"))

message = """
            To iterate over dictionary,
            use for loop with dict_var.keys() function.
            
            for key in dict1.keys():
                print(key, " = ", dict1[key])
          """  
print(message)

for key in dict1.keys():
    print(key, " = ", dict1[key])
    
message = """
            There is prefered way to do this,
            
            Using for loop with two variables & with dict_var.items() function.
            
            for key, value in dict1.items():
                print(key, " = ", value)
          """  
print(message) 

for key, value in dict1.items():
    print(key, " = ", value)

message = """
            Dictionaries contain many such operations, 
            check them out using help() & dir().
            
            help(dict.pop)
            print(dir(dict))
            
          """  
print(message)

help(dict.pop)
print(dir(dict))  