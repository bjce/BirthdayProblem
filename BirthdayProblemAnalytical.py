import numpy as np
import math
def BirthdayParty(n):
    return 1 - (math.factorial(365)/(365**n*math.factorial(365-n))) 
print(BirthdayParty(23))
