import Model

class Core:

    NoCores = 0;
      
    def __init__(self, id): # parametros: Id, PartList,  Util, UtilEfectiva, Nperdidas
		self.items =[]
		self.Id =id
		self.PartList =[]
		self.Util =0
		self.UtilEfectiva =0
		self.Nperdidas=0
		Core.NoCores +=1

       
    def ID(self):      # devuelve el Id
		return Id
            
    def coreParts(self):    # devuelve la lista de parts
		return self.PartList

    def coreAddPart(self, pid):
		self.PartList.append(pid)

    def coreAddPartU(self, pid, u):
		self.PartList.append(pid)
		self.Util += u
		    	
    def coreUtilEfectiva(self, u):   #pone la u efctiva
		self.UtilEfectiva=u
        
    def coreUtil(self):           #devuelve la util
		return self.Util

    def coreUtilEfectiva(self):	
		return self.UtilEfectiva
		
    def coreNumber(self):
		return Core.NoCores
        
    def show(self):
		print"Core(",self.Id,",",self.Util,")"
		for i in range(len(self.PartList)):
			pid=self.PartList[i]
			p = Model.partById(pid)
			p.show()

