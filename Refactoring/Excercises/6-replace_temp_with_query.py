# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        """
            Find, print, congratulate the school's graduates.
            Lastly, recommend the top graduates to top employers
        """
        self.find_graduates()
        self.print_graduates()
        self.congratulate_graduates()
        self.recommend_top_students_to_top_employers()

    def find_graduates(self):
        """Find the students in the school who have successfully graduated."""
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)
        self.passed_students = passed_students

    def print_graduates(self):
        """Print students who graduated."""
        print('*** Student who graduated *** ')
        for student in self.passed_students:
            print(student.name)
        print('****************************')

    def congratulate_graduates(self):
        """Send congrat emails to them."""
        for student in self.passed_students:
            student.send_congrat_email()

    def recommend_top_students_to_top_employers(self):
        """Get the top students to recommend to top employers."""
        percentile = 0.9
        top_10_percent = self.get_top_graduates(percentile)
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        self.recommend_graduates(top_10_percent, top_employers)

    def get_top_graduates(self, percentile):
        """Get top graduates based on the given percentile."""
        sorted_graduates = self.passed_students.sort(key=lambda student: student.get_gpa())
        index = int(percentile * len(sorted_graduates))
        top_10_percent = sorted_graduates[index:]
        return top_10_percent

    def recommend_graduates(self, graduates, employers):
        """Recommends graduates to employers."""
        for employer in employers:
            employer.send(graduates)

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
