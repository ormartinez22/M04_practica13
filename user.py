#creating a class user
class user:
    #making a method to define the self attributes of the class
    def salutation(self):
      #printing all attributes one by one
      print("The name of the user is : " + self.name) 
      print("The surname of the user is : " + self.surname)
      print("The age of the user is : " + self.age)
      print("The email of the user is : " + self.email)
      print("The phone number of the user is : " + self.phone)
      print("The profession of the user is : " + self.job)

#making the constructors or builders of the given class
    def __init__(self,name,surname,age,email,phone,job):
        #difining all the attributes of the constructor one by one
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.phone = phone
        self.job = job

#difining getter method for name
    def getName(self):
           return self.name


#difining setter method for name    
    def setName(self , name):
         self.name = name

#difining getter method for surname
    def getSurname(self):
       return self.surname


#difining setter method for surname    
    def setSurname(self , surname):
     self.surname = surname

#difining getter method for age
    def getAge(self):
      return self.age


#difining setter method for age    
    def setAge(self , age):
     self.age = age

#difining getter method for email
    def getEmail(self):
       return self.email


#difining setter method for email
    def setEmail(self , email):
       self.email = email

#difining getter method for phone
    def getPhone(self):
      return self.phone


#difining setter method for phone    
    def setPhone(self , phone):
     self.phone = phone 

#difining getter method for job
    def getJob(self):
     return self.job

#difining setter method for job    
    def setJob(self , job):
     self.job = job
