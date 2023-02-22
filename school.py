class school:#Definició de la classe

    #Definició del mètode que imprimeix els atributs de l'objecte
    def info(self):
        print("El nom de l'escola és: " +self.nom)
        print("Eltipus d'escola " +self.nom+ "és: " +self.tipus)
        print("La ciutat de l'escola" +self.nom+ "és: " +self.ciutat)
        print("El número d'aules de l'escola " +self.nom+ "és: " +str(self.numAules))
        print("El número de professors de l'escola " +self.nom+ "és: " +str(self.numProfessors))
        print("El número de despatxos de l'escola " +self.nom+ "és: " +str(self.numDespatxos))
    
    #Definicio del constructor amb 6 atributs, serveix per crear instancies de classe
    def __init__(self,nom,tipus,ciutat,numAules,numProfessors,numDespatxos):
        self.nom = nom
        self.tipus = tipus
        self.ciutat = ciutat
        self.numAules = numAules
        self.numProfessors = numProfessors
        self.numDespatxos = numDespatxos

    #Definició dels getters, serveixen per obtenir el valor dels atributs de les instàncies
    def getNom(self):
        return self.nom
    def getTipus(self):
        return self.tipus
    def getCiutat(self):
        return self.ciutat
    def getNumAules(self):
        return self.numAules
    def getNumProfessors(self):
        return self.numProfessors
    def getNumDespatxos(self):
        return self.numDespatxos
    
    #Definició dels setters, serveixen per modificar el valor dels atributs de les instàncies
    def setNom(self, nom):
        self.nom = nom
    def setTipus(self, tipus):
        self.tipus = tipus
    def setCiutat(self, ciutat):
        self.adreça = ciutat
    def setNumAules(self, numAules):
        self.numAules = numAules
    def setNumProfessors(self, numProfessors):
        self.numProfessors = numProfessors
    def setNumDespatxos(self, numDespatxos):
        self.numDespatxos= numDespatxos