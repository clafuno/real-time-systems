##Module: Utils
import random

Traces = {}
mcores = 0
Activations = {}
last = ""
lastTask = ""

def traceInit(ncores):
    global last

    mcores = ncores
    for i in range(ncores):
        Traces[i] = []
    Activations = {}
    last = ""

def traceExecBegin(ncore, time, taskId):
    global last, lastTask

    list = Traces[ncore]
    if (last == "B"):
        list.append((lastTask, "TE", time))

    list.append((taskId, "TB", time)) 
    #print "TB", time, taskId
    Traces[ncore] = list
    lastTask = taskId
    last = "B"
    if (Activations.has_key(taskId)):
        Activations[taskId] = Activations[taskId] + 1
    else:
        Activations[taskId] = 1

def traceExecEnd(ncore, time, taskId):
    global last, lastTask

    list = Traces[ncore]
    list.append((taskId, "TE", time)) 
    Traces[ncore] = list
    #print "TE", time, taskId
    last = "E"

    
def traceShow(ncore):
    res = ""
    trz = Traces[ncore]
    for i in range(len(trz)):
        if ("TB" in trz[i]):
            startTime = trz[i][2]
            res += trz[i][0] + " [" + str(startTime)
        elif ("TE" in trz[i]):
            endTime = trz[i][2]
            duration = endTime - startTime
            res += ", " + str(duration) + "]\n"
    print res
    print Activations