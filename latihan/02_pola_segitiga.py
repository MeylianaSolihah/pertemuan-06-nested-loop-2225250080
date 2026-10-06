n = int(input("n: "))

while n <= 0:
    n = int(input("Masukkan n positif: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()