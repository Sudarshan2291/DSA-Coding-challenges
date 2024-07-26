import math

enm_health = int(input("Enter the health of enemy"))
sp_attack = int(input("Enter the damage by special attack"))
np_attack = int(input("Enter the damage of normal attack"))

def min_no_attack(en_h, spd, npd):
    en_h = en_h - spd
    if en_h <= 0:
        return 1
    else:
        if en_h % npd == 0:
            return (en_h // npd) + 1
        else:
            return (en_h // npd) + 2
        
min_attack = min_no_attack(enm_health, sp_attack, np_attack)
print(min_attack)