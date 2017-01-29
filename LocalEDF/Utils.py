##Module: Tracer
import random

periods = [10 ,20 ,25 ,40 ,50 ,100 ,125 ,200 ,250 ,500 ,1000]

def adjust(v, nd):
	return float(float(round(v * 10**nd)) / 10**nd)
	
def UUniFastDiscard(n, u, nsets):
    sets = []
    while len(sets) < nsets:
        # Classic UUniFast algorithm:
        utilizations = []
        sumU = u
        for i in range(1, n):
            nextSumU = sumU * random.random() ** (1.0 / (n - i))
            utilizations.append(sumU - nextSumU)
            sumU = nextSumU
        utilizations.append(nextSumU)

        # If no task utilization exceeds 1:
        if not [ut for ut in utilizations if ut > 1]:
            sets.append(utilizations)

    return sets
    
def UUniFast(n, u):
    values = UUniFastDiscard(n, u, 1)
    utils = values[0]
    for i in range(len(utils)):
        utils[i] = adjust(utils[i], 4)
    return utils
    
    
def PeriodWCET (u):    #Determina el periodo y wcet que se ajusten a u. Periodo tiene que ser un elemento de periods
    per = random.choice(periods)
    wcet = int(u * per)
    if (wcet == 0):
    	wcet = 1
    return [per, wcet] 

def lcm(x,y):
    if x > y:
        greater = x
    else:
       greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
        greater += 1
    return lcm

def HyperPeriod(pers):    # determina el hiperperiodo de la lista de periodos 
    #print len(pers)
    hypPer = pers.pop()

    while len(pers) > 1:
        hypPer = lcm(hypPer,pers[len(pers)-1])
        k = pers.pop()
    return hypPer
