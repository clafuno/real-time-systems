import Model

class Partition:


    NoPartitions = 0;
      
    def __init__(self, id, Clevel, u):  # attributos: Id, CLevel, NoTasks, Util, UtilEfective, Core, TaskList
        self.Id = id
        self.CLevel = Clevel
        self.Util = u
        self.UtilEfective = 0
        self.Core = 0
        self.NoTasks = 0
        self.TaskList = []
        Partition.NoPartitions += 1

    def partId(self):
        return self.Id
        
    def partCLevel(self):
	    return self.CLevel
        
    def partUtil(self):
	    return self.Util

    def allocCore(self, cid):
	    self.Core = cid
	
	
    def partAddTask(self, tskId, u):
        self.TaskList.append(tskId)
        self.UtilEfective += u
        self.NoTasks += 1

    def partNumber(self):
        return  Partition.NoPartitions
        
    def show(self):
        print "  Partition(" +str(self.Id)+ ", " +str(self.CLevel)+ ", " +str(self.NoTasks)+", " +str(self.Util)+ ", " +str(self.UtilEfective)+ ", " +str(self.Core)+ " )"
        for i in range(len(self.TaskList)):
            t = Model.taskById(self.TaskList[i])
            t.show()
 
    def partTaskList(self):     #new Partition
        return self.TaskList