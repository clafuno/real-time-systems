##Module: BinPacking
import random

politicas = ("FF", "NF", "BF", "WF")
politica = ""
NBins = 0
Bins = []
Pesos = []
nextBin = 0
init = 0


def initBin(metodo, nbins):
    global politica,  NBins, Pesos, init, nextBin
    if (metodo in politicas): # checks if the policy is among the ones in list
        politica = metodo;
    else:
        raise Invalid_Param      # genera una excepcion si no existe

    if (nbins >0): #checks if the introduced # of bins is real
        NBins = nbins
    else:
        raise Invalid_Param

    #Bins = []
    for i in range(NBins):
        Bins.append([i,0.0,[]]) # List of bin - total weight - processes
    print Bins
    init = 1
    nextBin = 0
    print "Successful"

def binAdd(item, peso):
# "anade un item a una de las lista con un peso de acuerdo al metodo y criterio definido en initBins"
    #print "binAdd", item, peso

    try:
        if (politica is "FF"):
            binAddFF(item, peso)
        elif (politica is "NF"):
            binAddNF(item, peso)
        elif (politica is "BF"):
            binAddBF(item, peso)
        elif (politica is "WF"):
            binAddWF(item, peso)
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
        if (Pesos[i] + peso) <= 1: # If it fits
            Bins[i][2].append(item)
            Bins[i][1] += peso
            allocated = 1
            break

    # if Pesos.count(0.0) == NBins:
    #     #print "All bins are empty"
    #     Bins[0][2].append(item)
    #     Bins[0][1] += peso
    #     allocated = 1

    # else:
    #     sortedBins = sorted(Bins, key=lambda peso:peso[1])
    #     #print sortedBins
    #     i = Pesos.count(0)
    #     if (sortedBins[i][1] + peso) > 1:
    #         sortedBins[0][2].append(item)
    #         sortedBins[0][1] += peso
    #         allocated = 1
    #     else:
    #         sortedBins[i][2].append(item)
    #         sortedBins[i][1] += peso
    #         allocated = 1

    if (allocated == 0):
        raise

def binAddNF(item, peso):
    #print "addNF", item, peso
    global nextBin
    allocated = 0

    Pesos = []
    for i in range(NBins):
        Pesos.append(Bins[i][1])

    if (Pesos[nextBin] + peso) <= 1:
        print Pesos[nextBin], peso
        Bins[nextBin][2].append(item)
        Bins[nextBin][1] += peso
        allocated = 1
    else:
        nextBin = Pesos.index(0)
        print nextBin
        Bins[nextBin][2].append(item)
        Bins[nextBin][1] += peso
        allocated = 1


    # # Assign to the same core as last one
    # if Pesos.count(0.0) == NBins:
    #     #print "All bins are empty"
    #     Bins[0][2].append(item)
    #     Bins[0][1] += peso
    #     nextBin = 0
    #     allocated = 1
    # # if "occupation level + peso" > 1 --> Assign to 1st empty core
    # else:
    #     sortedBins = sorted(Bins, key=lambda peso:peso[1])
    #     #print sortedBins
    #     i = Pesos.count(0)
    #     if(Bins[nextBin][1] + peso) > 1:
    #         sortedBins[0][2].append(item)
    #         sortedBins[0][1] += peso
    #         nextBin = sortedBins[0][0]
    #         allocated = 1
    #     else:
    #         Bins[nextBin][2].append(item)
    #         Bins[nextBin][1] += peso
    #         allocated = 1

    if (allocated == 0):
        raise


def binAddBF(item, peso):
    #print "addBF", item, peso
    global Pesos
    allocated = 0
    capacity = [1] * NBins

    sortedBins = sorted(Bins, reverse=True, key=lambda peso:peso[1])
    #Count occurrences of max value

    for i in range(NBins):
        capacity[i] = 1 - sortedBins[i][1]
    print peso, item


    for i in range(NBins):
        #print i, capacity[i],peso
        if capacity[i] >= peso:
            sortedBins[i][2].append(item)
            sortedBins[i][1] += peso
            allocated = 1
            break

    # check "occupation level" of cores
    # Assign to the most occupied one
    # - IF same occupation --> Assign to lower index
    # if "occupation level + peso" > 1 --> Assign to 1st empty core

    if (allocated == 0):
        raise

def binAddWF(item, peso):
    #print "addWF", item, peso
    global Pesos
    allocated = 0
    capacity = [1] * NBins

    sortedBins = sorted(Bins, key=lambda peso:peso[1])
    #Count occurrences of max value

    for i in range(NBins):
        capacity[i] = 1 - sortedBins[i][1]
    print peso, item


    for i in range(NBins):
        #print i, capacity[i],peso
        if capacity[i] >= peso:
            sortedBins[i][2].append(item)
            sortedBins[i][1] += peso
            allocated = 1
            break


    # check "occupation level" of cores
    # Assign to the least occupied one
    # - IF same occupation --> Assign to lower index

    if (allocated == 0):
        raise


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
    return 1

def binDiscrepancy():
#    "devuelve una lista con las diferencias de peso de los bins. Por ejemplo: si la 0: 40, 1: 50, 2:60  3: 38"
#    "la funcion devolveria (2, 12, 22, 0) la minima es cero y el resto la diferencia respecto a la min"
    return 1

def show():
    spesos = 0.0
    Pesos = []
    for i in range(NBins):
        Pesos.append(Bins[i][1])

    for i in range(len(Pesos)):
        spesos += Pesos[i]
    print "Bins:", Bins, "\n Pesos:", Pesos, "Suma Pesos: ",spesos
    del Bins[:]
