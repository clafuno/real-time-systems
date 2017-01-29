###Module System
import Model

CoreList = []
PartitionList = []
Cores = 0
Util = 0.0

def defineSystem(mCores, gUtil):
    global Util, Cores, CoreList, PartitionList

    Util = gUtil
    Cores = mCores
    CoreList = []
    PartitionList = []
  
def numberCores():
	return Cores
            
def util():
	return Util

def addCore(c):
	global CoreList
	CoreList.append(c)
	 	
def addPartition(p):
	global PartitionList
	PartitionList.append(p)
    
def numberPartitions():
	return len(PartitionList)
        
def show():
	print "System (" ,Cores, Util, ")"
	print "N. Partitions (" ,numberPartitions(), ")"
	
	for i in range(numberCores()):
		cID = CoreList[i]
		c = Model.coreById(cID)
		c.show()
