def roll_call_dwarves(names):
    for i, name in enumerate(names):
        print(f'{i+1}. {name}')

def summon_captain_planet(list):
    return [f"{item.capitalize()}!" for item in list]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False         

def find_the_cheese(foods):
    for food in foods:
        if food == "cheddar":
            return "cheddar"
        if food == "gouda":
            return "gouda"
        if food == "camembert":
            return "camembert"
    else:
        return None    
