import random


def randomNumberGenerator(maxNumber): 
    """_summary_
    
    Args:
        `maxNumber` (Int): Maximum number that can be generated
    """
    number = random.randrange(0, maxNumber)
    
    return number

max = input('Please enter a maximum number: ')
print(randomNumberGenerator(int(max)))
