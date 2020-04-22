import random
import numpy as np

GroupSize = 40 
NumberSim = 5000
GlobalResults = []
for j in range(0,NumberSim):
    group = []
    for _ in range(0,GroupSize):
        group.append(random.randint(1,366))
    match = []
    for i in range(0, GroupSize):
        if group[i] in np.delete(group,i):
           match.append(True) 
        elif group[i] not in np.delete(group,i):
           match.append(False)
    if True in match:
        GlobalResults.append(True)
    else:
        GlobalResults.append(False)
prob = sum(GlobalResults)/len(GlobalResults)
print("The probability that at least 2 people have the same birthdate "\
      +	"\nin a group of {} people is {} (average of {} simulations)".format(GroupSize, prob, NumberSim))
