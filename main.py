from animal import animal 
from vehicle import vehicle
from school import school

elefant = animal("elefant",3,"mamífer",2.20,2100,"gris")
serp = animal("serp",1,"reptil",0.10,0.4,"negre")

cotxe = vehicle("cotxe","3322FG","Ford",200000,"negre",10000)
camio = vehicle("camio","1399TT","Toyota",300000,"blanc",20000)

jaumeBalmes = school("Jaume Balmes","Pública","Barcelona",30,25,15)
ernestLluch= school("Ernest Lluch","Pública","Barclona",50,60,20)

elefant.salutacio()
elefant.setPes(2300)
print("\n")
elefant.salutacio()
print("\n")
serp.salutacio()
serp.setColor("groc")
print("\n")
serp.salutacio()
print("\n")

cotxe.parts()
cotxe.setMarca("Toyota")
print("\n")
cotxe.parts()

print("\n")
camio.parts()
camio.setColor("gris")
print("\n")
camio.parts()
print("\n")
jaumeBalmes.info()
jaumeBalmes.setNumProfessors(40)
print("\n")
jaumeBalmes.info()
print("\n")
ernestLluch.info()
ernestLluch.setNumDespatxos(11)
print("\n")
ernestLluch.info()