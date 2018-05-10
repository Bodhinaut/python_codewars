
"""
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
"""

# Updated version refactored below

def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
