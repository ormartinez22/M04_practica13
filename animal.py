class animal:#Definició de la classe

    #Definició del mètode que imprimeix els atributs de l'objecte
    def salutacio(self):
        print("El nom de l'animal és: " +self.nom)
        print("L'edat és: " +str(self.edat))
        print("El tipus és: " +self.tipus)
        print("L'altura és: " +str(self.altura))
        print("El pes és: " +str(self.pes))
        print("El color és: " +self.color)
    
    #Definicio del constructor amb 6 atributs, serveix per crear instancies de classe
    def __init__(self,nom,edat,tipus,altura,pes,color):
        self.nom = nom
        self.edat = edat
        self.tipus = tipus
        self.altura = altura
        self.pes = pes
        self.color = color

    #Definició dels getters, serveixen per obtenir el valor dels atributs de les instàncies
    def getNom(self):
        return self.nom
    def getEdat(self):
        return self.edat
    def getTipus(self):
        return self.tipus
    def getAltura(self):
        return self.altura
    def getPes(self):
        return self.pes
    def getColor(self):
        return self.color
    
    #Definició dels setters, serveixen per modificar el valor dels atributs de les instàncies  
    def setNom(self, nom):
        self.nom = nom
    def setEdat(self, edat):
        self.edat = edat
    def setTipus(self, tipus):
        self.tipus = tipus
    def setAltura(self, altura):
        self.altura = altura
    def setPes(self,pes):
        self.pes = pes
    def setColor(self, color):
        self.color = color
