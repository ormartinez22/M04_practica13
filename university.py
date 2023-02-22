#creating a class university
class university:
    #making a method to define the self attributes of the class
    def info(self):
      #printing all attributes one by one
      print("The name of the university is : " + self.name) 
      print("The campus of the university is : " + self.campus)
      print("The location of the university is : " + self.location)
      print("The department of the university is : " + self.departments)
      print("The total professors of the university are : " + self.professors)
      print("The total students of the university are : " + self.students)

#making the constructors or builders of the given class
    def __init__(self,name,campus,location,departments,professors,students):
        #difining all the attributes of the constructor one by one
        self.name = name
        self.campus = campus
        self.location = location
        self.departments = departments
        self.professors = professors
        self.students = students

#difining getter method for name
    def getName(self):
           return self.name

#difining setter method for name    
    def setName(self , name):
         self.name = name

#difining getter method for campus
    def getCampus(self):
       return self.campus


#difining setter method for campus    
    def setCampus(self , campus):
     self.campus = campus

#difining getter method for location
    def getLocation(self):
      return self.location


#difining setter method for location    
    def setLocation(self , location):
     self.location = location

#difining getter method for departments
    def getDepartments(self):
       return self.departments


#difining setter method for departments
    def setDepartments(self , departments):
       self.departments = departments

#difining getter method for professors
    def getProfessors(self):
      return self.professors


#difining setter method for professors    
    def setProfessors(self , professors):
     self.professors = professors 

#difining getter method for students
    def getStudents(self):
     return self.students


#difining setter method for students    
    def setStudents(self , students):
     self.students = students
