# ATM Money Widraw Problem

K = int(input("Enter the the money in ATM: "))
N = int(input("Enter number of peoples in Queue: "))
N_amt = []
# code for the amount money required ith member in queue
for i in range(N):
    N_amt.append(int(input(f"Enter the amount required to {i} person: ")))

def money_queue(K,N,N_amt):
    s = ''
    money = K
    for i in range(N):
        if N_amt[i] > money:
            s += '0'
        else:
            s += '1'
            money -= N_amt[i]
    return s

res = money_queue(K,N,N_amt)
print(res)

