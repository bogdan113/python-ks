'''
Created on Jun 16, 2014

@author: canca
'''

thisfile = open("text.csv")

class Student:
    def __init__(self, name, math_grade, info_grade, chemistry_grade, physics_grade, comments):
        self.name = name
        self.math_grade = math_grade
        self.info_grade = info_grade
        self.chemistry_grade = chemistry_grade
        self.physics_grade = physics_grade
        self.comments = comments
    def __str__(self):
        return '%(name)s has %(math)d grade in math, %(info)d grade in info, %(chemistry)d grade in chemistry, %(physics)d grade in physics.' \
            % {"name":self.name, "math":self.math_grade, "info":self.info_grade, "chemistry":self.chemistry_grade, "physics":self.physics_grade} 

my_dict = {}

for index, eachline in enumerate(thisfile):
    print(index, eachline)
    student_raw = eachline.split(",")
    student = Student(student_raw[0], int(student_raw[1]), int(student_raw[2]), \
                       int(student_raw[3]), int(student_raw[4]), student_raw[5:len(student_raw)])
    my_dict[index] = student

print my_dict[0]

for x in filter(lambda (index, item): item.math_grade == 10, my_dict.items()):
    print(x[1])
