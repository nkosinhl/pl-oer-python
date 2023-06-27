def generate(data):
    data["params"]["names_for_user"] = []
    data["params"]["names_from_user"] = [
        {
            "name": "string_indicating_negativity",
            "description": "Function to return string based on whether given number is negative or not",
            "type": "python function",
        }
    ]
