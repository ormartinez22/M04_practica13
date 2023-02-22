class vehicle: #Definició de la classe

    #Definició del mètode que imprimeix els atributs de l'objecte
    def parts(self): 
        print("El tipus de vehicle és: " +self.tipus)
        print("La matricula de " +self.tipus+ "és: " +self.matricula)
        print("La marca de " +self.tipus+ "és: " +self.marca)
        print("El preu del " +self.tipus+ "és: " +str(self.preu))
        print("El color del " +self.tipus+ "és: " +self.color)
        print("El pes del " +self.tipus+ "és: " +str(self.pes))

    #Definicio del constructor amb 6 atributs, serveix per crear instancies de classe
    def __init__(self,tipus,matricula,marca,preu,color,pes): 
        self.tipus = tipus
        self.matricula = matricula
        self.marca = marca
        self.preu = preu
        self.color = color
        self.pes = pes
    
    #Definició dels getters, serveixen per obtenir el valor dels atributs de les instàncies
    def getTipus(self):
        return self.tipus
    def getMatricula(self):
        return self.matricula
    def getMarca(self):
        return self.marca
    def getPreu(self):
        return self.preu
    def getColor(self):
        return self.color
    def getPes(self):
        return self.pes
    
    #Definició dels setters, serveixen per modificar el valor dels atributs de les instàncies
    def setTipus(self, tipus):
        self.tipus = tipus
    def setMatricula(self, matricula):
        self.matricula = matricula
    def setMarca(self, marca):
        self.marca = marca
    def setPreu(self, preu):
        self.preu = preu
    def setColor(self, color):
        self.color = color
    def setPes(self, pes):
        self.pes = pes