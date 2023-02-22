#creating a class book
class book:
    #making a method to define the self attributes of the class
    def bookStore(self):
      #printing all attributes one by one
      print("The title of the book is : " + self.title) 
      print("The author of the book is : " + self.author)
      print("The total pages of the book are : " + self.pages)
      print("The kind of the book is : " + self.kind)
      print("The published year of the book is : " + self.year)
      print("The total copies of the book are : " + self.copies)

#making the constructors or builders of the given class
    def __init__(self,title,author,pages,kind,year,copies):
        #difining all the attributes of the constructor one by one
        self.title = title
        self.author = author
        self.pages = pages
        self.kind = kind
        self.year = year
        self.copies = copies

#difining getter method for title
    def getTitle(self):
           return self.title

#difining setter method for title    
    def setTitle(self , title):
         self.title = title

#difining getter method for author
    def getAuthor(self):
       return self.author

#difining setter method for author    
    def setAuthor(self , author):
     self.author = author

#difining getter method for pages
    def getPages(self):
      return self.pages

#difining setter method for pages    
    def setPages(self , pages):
     self.pages = pages

#difining getter method for kind of the book
    def getKind(self):
       return self.kind

#difining setter method for kind of the book
    def setKind(self , kind):
       self.kind = kind

#difining getter method for year
    def getYear(self):
      return self.year

#difining setter method for year    
    def setYear(self , year):
     self.year = year 

#difining getter method for copies
    def getCopies(self):
     return self.copies

#difining setter method for copies    
    def setCopies(self , copies):
     self.copies = copies
