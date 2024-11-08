

class student:
    def __init__(self, name):
        self.name = name
        self._testscores=[]

    def setName(self,othername):
        self.name=othername

    def  addTest(self,score):
        self._testscores.append(score)
    def  getTestScores(self):
        return self._testscores
    
    def getName(self):
        return self.name

# Create an empty list called roster
roster = []

# Initialize a flag to control the loop
add_more_students = True

# Prompt the user to enter a student name
while add_more_students:
    name = input("Enter student name (or press <enter> to stop): ")
    if name == "":
        add_more_students = False  # Exit the loop if the user presses <enter>
    else:
        # Create a new student object with the name entered
        new_student = student(name)

        # Prompt the user to enter test scores
        add_more_scores = True
        while add_more_scores:
            score_input = input(f"Enter a test score for {name} (or press <enter> to stop): ")
            if score_input == "":
                add_more_scores = False  # Exit the loop if the user presses <enter>
            else:
                try:
                    score = float(score_input)  # Convert input to float
                    new_student.addTest(score)  # Add the score to the student object
                except ValueError:
                    print("Please enter a valid number for the test score.")

        # Add the student object to roster
        roster.append(new_student)

# After exiting the loops, you can print the roster to verify
print("\nRoster of Students:")
for student in roster:
    print(f"Name: {student.getName()}, Test Scores: {student.getTestScores()},")