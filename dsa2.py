
no_sold = int(input("Enter number of soldiers"))
weapons = []

for i in range(no_sold):
    weapons.append(int(input(f"enter number of wepons have {i+1}th soldier ")))

def army_status(no_soldier, weapons):
    lucky = 0
    unlucky = 0
    for i in range(no_soldier):
        if (weapons[i] % 2) == 0:
            lucky += 1
        else:
            unlucky += 1
    
    if lucky > unlucky:
        return "Ready for battle"
    else:
        return "Not ready for battle"

status = army_status(no_sold, weapons)
print(status)