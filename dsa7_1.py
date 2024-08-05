""" One city with three political parties total population is 101 majority is  50 
    parties are A,B,C """


total_vote = 101
majority = 50
vote_A = int(input("enter the votes of party A: "))
vote_B = int(input("enter the votes of party B: "))
vote_C = total_vote - vote_A - vote_B

def win_party(vote_A,vote_B,vote_C):
    if vote_A >= 50:
        print("party A win")
    elif vote_B >= 50:
        print("party B win")
    elif vote_C >= 50:
        print("party C win")
    else:
        print("NOTA")

win_party(vote_A,vote_B,vote_C)

