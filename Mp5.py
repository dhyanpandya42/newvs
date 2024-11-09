# MACHINE PROBLEM 5
# DHYAN PANDYA
#
#DESCRIPTION:THESE PROGRAM DEFINES A CLASS STUDENT,,CONTAINS STUID,NAME,TESTSCORES,AVG
# TAKES DATA FROM THE TEXT FILE AND DISPLAYS IT
# ATLAST IT CAN ADD STUDENT NAME OR TEST SCORES TO THE WHOLE LIST

class  Student:
## Student Class Definition 
# ## 4 Instance Variables:
# _stuID str - 5 characters, 2 alpha (initials), 3 numeric (random) 
# _name list - 2 str elements, first name, last name
# _testScores list - int values (could be empty, no tests taken) # _avg float - the average of _testScores (0.0 if no tests taken) ## Constructor:
## __init__(self, stuID) Initialize _stuId to stuID, _name to a list with 2 empty str elements, _testScores to the empty list, # _avg to 0.0
## __str__ is defined for our class (the str conscructor)

    def __init__(self, stuID):
        self._stuID = stuID
        self._name = ["", ""]
        self._testScores = []
        self._avg = 0.0
    def __str__(self):
        # return f'student: {self._stuID} {self._name[0]} {self._name[1]} 'f



        return f"Student: {self._stuID} {self._name[0]} {self._name[1]}\n" \
               f"Test Scores: {' '.join(map(str, self._testScores))}\n" \
               f"Test Average: {self._avg:.2f}"
      
    def getID(self):
        return self._stuID
    def getName(self):
        return self._name[0] + " " + self._name[1]
    
    def setName(self, firstName, lastName):
        self._name[0] = firstName
        self._name[1] = lastName

    def getScores(self):
        return self._testScores
    
    def getAvg(self):
        if len(self._testScores) == 0:
            return 0.0
        return self._avg
    
    def addTest(self, score):
        self._testScores.append(score)
        self._avg = sum(self._testScores) / len(self._testScores)

    def _CalcAvg(self):
        if  len(self._testScores) == 0:
            self._avg=0.0
        else:
            self._avg=sum(self._testScores) / len(self._testScores)

def getStudents():
## Opens the data file of student info... studentID, firstName, lastName, then # testScores - the number of test scores is variable, from zero up... reads 
# # each line of data as a str, divides the line into the values... str, str, str,
#  # int, int, int... (a variable number of int values - could be none)... 
# # instantiates a new Student object, uses the Student object's instance methods 
# # to add those values to the object, adds the Student object to a dict of objects,
#  # and returns the dict of Student objects.
## There are no parameters. ## Returns a dict of objects from the Student class #
   roster = {}
   with open('MP5Data.txt', 'r') as file:
       for  line in file:
           values = line.strip().split()
           stuID=values.pop(0)
           firstName=values.pop(0)
           lastName=values.pop(0)
        #    testScores =[]
        #    for score in  values:
        #        testScores.append(int(score))
        #        values.pop(0)
        #    student = Student(stuID)
        #    student.setName(firstName, lastName)
        #    for score  in testScores:
        #        student.addTest(score)
        #    roster[stuID]=student
           testScores = list(map(int, values))
           student = Student(stuID)
           student.setName(firstName, lastName)
           for score in testScores:
                student.addTest(score)
           roster[stuID] = student
   return roster

def updateName(roster,stuID):
    firstName=input('First  Name: ')
    lastName=input('Last Name: ')
    
    roster[stuID].setName(firstName, lastName)



def updateTest(roster,stuID):
    testScore=input('Enter a test score (<Enter> to stop): ')
    while testScore:

        roster[stuID].addTest(int(testScore))
        testScore=input('Enter a test score (<Enter> to stop): ')


roster=getStudents()

for student in  roster:
    print(student)

stuID=input('Enter a  student ID(<Enter> to stop): ')
while stuID:
    if stuID in roster:
        print(roster[stuID])
        choice = input("(1) Change the Name\n(2) Add a Test\nWhat would you like to do? (<enter> to stop): ")
        if choice == '1':
            updateName(roster,stuID)
        elif  choice == '2':
            updateTest(roster,stuID)
    else:
        print("This student does not exist. You may enter the info now.")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        newStudent = Student(stuID)
        newStudent.setName(firstName, lastName)
        testScore=input('Enter a test score (<Enter> to stop): ')
        while testScore:
            newStudent.addTest(int(testScore))
            testScore=input('Enter a test score (<Enter> to stop): ')
        roster[stuID] = newStudent
        print("New Student Added:")
        print(newStudent)
    stuID=input('Enter a  student ID(<Enter> to stop): ')








           


            

        


    
        
