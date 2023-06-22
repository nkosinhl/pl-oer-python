def generate(data):
    data["params"]["names_for_user"] = []
    data["params"]["names_from_user"] = [
        {
            "name": "string_indicating_negativity",
            "description": "Function to compute the $n^\\text{th}$ Fibonacci number",
            "type": "python function",
        }
    ]
