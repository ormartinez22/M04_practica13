from animal import animal 
from vehicle import vehicle
from school import school

from book import book
from user import user
from university import university

elefant = animal("elefant",3,"mamífer",2.20,2100,"gris")
serp = animal("serp",1,"reptil",0.10,0.4,"negre")

cotxe = vehicle("cotxe","3322FG","Ford",200000,"negre",10000)
camio = vehicle("camio","1399TT","Toyota",300000,"blanc",20000)

jaumeBalmes = school("Jaume Balmes","Pública","Barcelona",30,25,15)
ernestLluch= school("Ernest Lluch","Pública","Barclona",50,60,20)

tree = book("falling leaves","Elif","156","nature","1985","618")
videoGames = book("Alexandra","mark","814","Tech","2015","561")

aQeedat = user("Aqeedat","NAbi","19","anabi@gmail.com","012365478","student")
oriol = user("Oriol","Martinez","31","omart@gmail.com","777777777","student")

upc = university("upc","nord","barcelona","tech","356","589")
uab = university("uab","sur","barcelona","art","6598","698")

tree.bookStore()
tree.setAuthor("Murat")
print("\n")
tree.bookStore()
print("\n")

aQeedat.salutation()
print("\n")
aQeedat.setAge("20")
aQeedat.salutation()
print("\n")

upc.info()
upc.setLocation("madrid")
print("\n")
upc.info()
print("\n")

elefant.salutacio()
elefant.setPes(2300)
print("\n")
elefant.salutacio()
print("\n")

serp.salutacio()
print("\n")
serp.setColor("groc")
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