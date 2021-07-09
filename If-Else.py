n = int(input())

if 1 <= n <= 100:
    if (n % 2 == 0 and n in range(2, 6)) or (n % 2 == 0 and n > 20):
        print("Not Weird")
    elif (n % 2 == 0 and n in range(6, 21)) or (n % 2 != 0):
        print("Weird")
