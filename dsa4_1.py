# IPL Team qualify calculate minimum matches to play
# Win 2 pt  lose 0 pt tie 1 pt

X = int(input("Enter the point required to qualify team: "))
Y = int(input("Enter the number of matches are remaining: "))

def cal_min_matches(x, y):
    if x%2 == 0:
        if x//2 <= Y:
            return x//2
        else:
            return -1
    
    else:
        if (x//2)+1 <= y:
            return (x//2)+1 
        else: 
            return -1
        
res = cal_min_matches(X, Y)
print(res)
