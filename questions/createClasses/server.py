# import prairielearn as pl

def generate(data):

    names_for_user = [
        {"name": "student_info", "description": "A tuple containing student netid, major and age information", "type": "tuple"},
    ]
    names_from_user = [
        {"name": "student_obj", "description": "The Student object containing information of <code>student_info</code>", "type": "Student"},
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    return data
