#Exercise 1 - person characteristics
import datetime
from typing import List, Tuple, Dict, Set

first_name = 'Dominik'
second_name = 'Szoboszlai'
dob = datetime.date(2000, 10, 25)
height_metres = 1.86
clubs = ['Liefering', 'Red Bull Salzburg', 'Red Bull Leipzig']
intl_caps = 26
intl_goals = 6
games_per_goal = intl_caps / intl_goals
position = 'Attacking Midfielder'
transfer_fee = '£25,000,000'

print(first_name, second_name)
print("Position:", position)
print("DOB:",dob)
print ("Height:", height_metres,"m")
print ("Average Games Per Goal", games_per_goal)
print("Transfer Fee", transfer_fee)

skills = ["finishing", "heading", "passing", "speed", "tackling"]

print("skills =",skills)

favourite_skill = input("What Is Your Favourite Skill?:")

#if list elements not included in another
if favourite_skill not in skills:
    skills.append(favourite_skill)

else :
    print("that skill already exists")

print(favourite_skill)
print(skills)

skill_dict = {'finishing':81,'heading':65,'passing':85,'speed':73,'tackling':45}
skill_input = input("Input Skill Here:")
skill_num = skill_dict[skill_input] if skill_input in skill_dict else None
if skill_num is None:
    print("no such skill")
elif skill_num > 80 : print("SUPER COOL")
elif skill_num >50 : print("COOL")

def higher_than(dict:Dict,number:int) :
    list_values = []
    for key,value in dict.items() :
        if value >= number :
           list_values.append(key)
    return list_values

print(higher_than(skill_dict,80))
