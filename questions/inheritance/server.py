# import prairielearn as pl

def generate(data):

    names_for_user = [
        {"name": "company_info", "description": "A tuple containing company name, head and services information", "type": "tuple"},
    ]
    names_from_user = [
        {"name": "it_company_obj", "description": "The ITCompany object containing information of <code>company_info</code>", "type": "ITCompany"},
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    return data
