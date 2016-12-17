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

    for i in range(NBins):
        Bins.append([i,0.0,[]]) # List of bin - total weight - processes
    init = 1
    nextBin = 0
    print "Successful"

def binAdd(item, peso):
# "anade un item a una de las lista con un peso de acuerdo al metodo y criterio definido en initBins"
    #print "binAdd", item, peso

    try:
        if (politica is "FF"):
            print "Policy FF"
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
    print "addFF", item, peso, NBins
    global Pesos
    allocated = 0
    # Sort list of bins according to weight
    sortedBins = sorted(Bins, key=lambda peso:peso[1])
    print sortedBins
    

    if sortedBins[1].count(0.0) == NBins:
        print "All bins are empty"
        sortedBins[0][2].add(item)
        sortedBins[0][1] += peso
        allocated = 1
    else:
        print "Hey there"

    # if sortedBins.count(0) == NBins:
    #     Bins[0].add(item)
    #     Pesos[0] += peso
    #     allocated = 1
    #     print "Allocated!"

    # else:
    #     if (Pesos[Pesos.count(0)] + peso) <= 1:
    #         Bins[Pesos.count(0)].add(item)
    #         Pesos[Pesos.count(0)] += peso 
    #         allocated = 1
    #         print "Allocated!"

    #     else:
    #         Bins[Pesos.count(0)-1].add(item)
    #         Pesos[Pesos.count(0)-1] += peso 
    #         allocated = 1
    #         print "Allocated!"

    # # Assign to the least occupied BUT != 0
    # # if "occupation level + peso" > 1 --> Assign to 1st empty core
    
    # if (allocated == 0):
    #     raise

def binAddNF(item, peso):
    #print "addNF", item, peso
    global nextBin
    allocated = 0
    # Assign to the same core as last one
    # if "occupation level + peso" > 1 --> Assign to 1st empty core

    if (allocated == 0):
        raise


def binAddBF(item, peso):
    #print "addBF", item, peso
    global Pesos
    allocated = 0
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
    for i in range(len(Pesos)):
        spesos += Pesos[i]
    print "Bins:", Bins, "\n Pesos:", Pesos, "Suma Pesos: ",spesos


