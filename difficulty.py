
import random



def difficulty(user_difficulty):
    
    if user_difficulty == 1:
        numbers = (random.randint(0,9), random.randint(0,9))
    elif user_difficulty == 2:
        numbers = (random.randint(10,99), random.randint(10,99))
    elif user_difficulty == 3:
        numbers = (random.randint(100,999), random.randint(100,999))
    return numbers
