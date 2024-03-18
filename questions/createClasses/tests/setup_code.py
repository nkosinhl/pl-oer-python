import numpy as np

def generate_student_tuple():
    major_list = ["bioe", "aero", "cee", "me", "chbe", "mse", "se", "ie", "abe"]
    random_i = np.random.randint(10,15)
    random_j = np.random.randint(1,3)

    student_id = chr(97+random_i) + chr(97+random_i+random_j) + str(np.random.randint(101,999))
    student_major = major_list[np.random.randint(0,9)]
    student_age = str(np.random.randint(18,23))
    return (student_id, student_major, student_age)

student_info = generate_student_tuple()