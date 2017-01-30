##Module: BinPacking
import random
import Core

politicas = ("FF", "NF", "BF", "WF")
politica = ""
NBins = 0
Bins = []
Pesos = []
nextBin = 0
init = 0
globalUtil = 0


def initBin(metodo, nbins, globalU):
    global politica,  NBins, Pesos, init, nextBin, globalUtil
    if (metodo in politicas): # checks if the policy is among the ones in list
        politica = metodo;
    else:
        raise Invalid_Param      # genera una excepcion si no existe

    if (nbins >0): #checks if the introduced # of bins is real
        NBins = nbins
    else:
        raise Invalid_Param

    globalUtil = globalU

    #Bins = []
    for i in range(NBins):
        Bins.append([i,0.0,[]]) # List of bin - total weight - processes
    #print Bins
    init = 1
    nextBin = 0

def binAdd(item, peso):
# "anade un item a una de las lista con un peso de acuerdo al metodo y criterio definido en initBins"
    #print "binAdd", item, peso
    try:
        if (politica is "FF"):
            return binAddFF(item, peso)
        elif (politica is "NF"):
            return binAddNF(item, peso)
        elif (politica is "BF"):
            return binAddBF(item, peso)
        elif (politica is "WF"):
            return binAddWF(item, peso)
    except:
        raise

def binAddFF(item, peso):
    #print "addFF", item, peso, NBins
    global Pesos
    allocated = 0

    Pesos = []
    for i in range(NBins):
        Pesos.append(Bins[i][1])
    #print Pesos

    for i in range(NBins):
        if (Pesos[i] + peso) <= globalUtil: # If it fits
            Bins[i][2].append(item)
            Bins[i][1] += peso
            allocated = 1
            return i

    if (allocated == 0):
        print "Error"
        return -1

def binAddNF(item, peso):
    #print "addNF", item, peso
    global nextBin
    allocated = 0

    Pesos = []
    for i in range(NBins):
        Pesos.append(Bins[i][1])

    if (Pesos[nextBin] + peso) <= globalUtil:
        #print Pesos[nextBin], peso
        Bins[nextBin][2].append(item)
        Bins[nextBin][1] += peso
        allocated = 1
        return i
    else:
        nextBin = Pesos.index(0)
        #print nextBin
        Bins[nextBin][2].append(item)
        Bins[nextBin][1] += peso
        allocated = 1
        return i

    if (allocated == 0):
        print "Error"
        return -1


def binAddBF(item, peso):
    #print "addBF", item, peso
    global Pesos
    allocated = 0
    capacity = [1] * NBins

    sortedBins = sorted(Bins, reverse=True, key=lambda peso:peso[1])
    #Count occurrences of max value

    for i in range(NBins):
        capacity[i] = globalUtil - sortedBins[i][1]
    #print peso, item


    for i in range(NBins):
        #print i, capacity[i],peso
        if capacity[i] >= peso:
            sortedBins[i][2].append(item)
            sortedBins[i][1] += peso
            allocated = 1
            return i
            break

    if (allocated == 0):
        print "Error"
        return -1

def binAddWF(item, peso):
    #print "addWF", item, peso
    global Pesos
    allocated = 0
    capacity = [1] * NBins

    sortedBins = sorted(Bins, key=lambda peso:peso[1])
    #Count occurrences of max value

    for i in range(NBins):
        capacity[i] = globalUtil - sortedBins[i][1]
    #print peso, item


    for i in range(NBins):
        #print i, capacity[i],peso
        if capacity[i] >= peso:
            sortedBins[i][2].append(item)
            sortedBins[i][1] += peso
            allocated = 1
            return i
            break

    if (allocated == 0):
        print "Error"
        return -1


def binGetbyIndex(idx):
#    "devuelve una lista con una lista de items y su peso (("P1", "P2"), 0,87)"
    return 1

def binGetAll():
#    "devuelve todas las listas de cada bin y una lista con los pesos"
    return 1

def binUtil(idx):
#    "devuelve el peso de la lista identificada or idx"
    return 1

def binUtilAll():
#    "devuelve la lista de los pesos"
	# global NBins
	# Pesos = []
 #    for i in range(NBins):
 #        Pesos.append(Bins[i][1])
	return 1

def binDiscrepancy():
#    "devuelve una lista con las diferencias de peso de los bins. Por ejemplo: si la 0: 40, 1: 50, 2:60  3: 38"
#    "la funcion devolveria (2, 12, 22, 0) la minima es cero y el resto la diferencia respecto a la min"
    return 1

def show():
    spesos = 0.0
    dicBin = {}
    Pesos = []
    
    for i in range(NBins):
        Pesos.append(Bins[i][1])

    for i in range(NBins):
    	dicBin[i] = Bins[i][2]

    for i in range(len(Pesos)):
        spesos += Pesos[i]
    print "Bins:", dicBin, "\n Pesos:", Pesos, "Suma Pesos: ",spesos
    del Bins[:]
