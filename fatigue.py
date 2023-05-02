import random

def fatigue(correct):
    
    phrase = random.randint(1,4)
    if correct == True:
        if (phrase == 1):
            return "\nVery good!"
        elif (phrase == 2):
            return "\nExcellent!"
        elif (phrase == 3):
            return "\nNice work!"
        else:
            return "\nKeep up the good work!"
    else:
        if (phrase == 1):
            return "\nNo, please try again."
        elif (phrase == 2):
            return "\nWrong, try once more."
        elif (phrase == 3):        
            return "\nDon't give up!"
        else:
            return "\nNo, keep trying."