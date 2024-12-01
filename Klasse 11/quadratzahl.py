def f(n):
    if n <= 1:
        return 1
    else:
        return (f(n-1) + f(n-2))

n = int(input("Gib' eine Zahl n ein: "))
for i in range(n+1):
    print(f(i))