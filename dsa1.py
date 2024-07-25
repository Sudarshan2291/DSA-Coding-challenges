n = int(input("number of dice roll"))
modi = []
rahul = []

for i in range(n):
    modi.append(int(input(f"enter {i+1} roll number of modi")))
    rahul.append(int(input(f"enter {i+1} roll number of rahul")))

def election_result(n,modi,rahul):
    for i in range(n):
        mx11 = max(modi)
        modi.remove(mx11)
        mx12 = max(modi)

        mx21 = max(rahul)
        rahul.remove(mx21)
        mx22 = max(rahul)

        if (mx11 + mx12) > (mx21 + mx22):
            return "winner is modi"

        elif (mx21 + mx22) > (mx11 + mx12):
            return "winner is rahul"

        else:
            return "tie"

result = election_result(n,modi,rahul)
print(result)
