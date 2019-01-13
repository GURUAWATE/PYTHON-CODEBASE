message = """
           temp = int(input("Enter a Number: "))   #input() returns a string, Hence casting is necessary.
           
           if (temp % 2) == 0:
               print("\\nThe Number is Even")
           else:
               print("\\nThe Number is Odd")
          """
print(message)  

temp = int(input("Enter a Number: "))
           
if (temp % 2) == 0:
    print("\nThe Number is Even")
else:
    print("\nThe Number is Odd")

message = """
           Scalene Triangle: All sides have diffrent lengths.
           Isosceles Triangle: Two of the sides have same lengths.
           Equilateral Triangle: All of the sides have same lengths.
           
           print("Enter 3 sides of a Triangle, To determine it's type: ")
           
           a = int(input("a: "))
           b = int(input("b: "))
           c = int(input("c: "))
           
           if (a == b):
                if(b == c):
                    print("\\nIt is a Equilateral Triangle")
                else: 
                    print("\\nIt is a Isosceles Triangle")
           else:
               print("\\nIt is a Scalene Triangle")
          """
print(message) 

print("\nEnter 3 sides of a Triangle, To determine it's type: ")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
         
if (a == b):
    if(b == c):
        print("\nIt is a Equilateral Triangle")
    else: 
        print("\nIt is a Isosceles Triangle")
else:
    print("\nIt is a Scalene Triangle")