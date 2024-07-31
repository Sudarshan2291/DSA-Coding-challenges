# Two friends gives examination of 3 DSA,TOC,DM subjects 100 marks each find whose rank bigger
""" cond 1)bigger total bigger rank. 2)total tie high DSA high rank. 3)total and DSA tie high TOC high rank
         4) all are tie get same rank """
# return A or B or A B

m1 = input("three space seprate integer denoting score of A: ").split()
m2 = input("three space seprate integer denoting score of B: ").split()

def highscorer(m1,m2):
    x = int(m1[0]) + int(m1[1]) + int(m1[2])
    y = int(m2[0]) + int(m2[1]) + int(m2[2])

    if x > y:
        return 'A'
    
    elif y > x:
        return 'B'
    
    else:
        if int(m1[0]) > int(m2[0]):
            return 'A'
        
        elif int(m2[0]) > int(m1[0]):
            return 'B'
        
        else:
            if int(m1[1]) > int(m2[1]):
                return 'A'

            elif int(m2[1]) > int(m1[1]):
                return 'B'

            else:
                return 'A B'

res = highscorer(m1,m2)
print(res)