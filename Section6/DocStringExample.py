import random


def randomNumberGenerator(maxNumber): 
    """_summary_
    
    param:
        `maxNumber` (Int): Maximum number that can be generated
    retruns:
        `number` (int): A random number between 0 and maxNumber
    """
    number = random.randrange(0, maxNumber)
    
    return number

max = input('Please enter a maximum number: ')
print(randomNumberGenerator(int(max)))
