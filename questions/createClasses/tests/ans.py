class Student:
    def __init__(self, netid, major, age):
        self.netid = netid
        self.major = major
        self.age = age

stu_netid, stu_major, stu_age = student_info
stu_major_upper = stu_major.upper()
stu_age_int = int(stu_age)
student_obj = Student(netid=stu_netid, major=stu_major_upper, age=stu_age_int)