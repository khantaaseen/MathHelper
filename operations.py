import random

def operations(user_operation):
    
    sign = ["+","-","*","/"]
    
    if user_operation == 1:
        sign = "+"
    elif user_operation == 2:
        sign = "-"
    elif user_operation ==3:
        sign = "*"
    elif user_operation == 4:
        sign = "/"
    elif user_operation == 5:
        sign = random.choice(sign)
    return sign
