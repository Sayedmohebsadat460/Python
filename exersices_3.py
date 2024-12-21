#  Operators
num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))
operator = input("Choose your operator between + , -  ,*  , / ")

if operator == "+" :
    print( num_1 +  num_2 )
elif operator == "-":
        print( num_1 - num_2 )
elif operator == "*":
        print( num_1 * num_2 )
elif operator == "/":
        print( num_1 / num_2 )      
else : 
       print("Invalid Entry!")