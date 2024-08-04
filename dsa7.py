# Candy game

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    limak, bob = 0, 0
    for i in range(1, 1000):  # A large enough range to cover all possible scenarios
        if i % 2 == 0:
            bob += i
            if bob > b:
                print("Limak")
                break
        else:
            limak += i
            if limak > a:
                print("Bob")
                break