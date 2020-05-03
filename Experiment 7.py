A = int(input("Enter a number between 0 and 1000: "))
if 0<=A<=1000:
    for b in range(A+1):
        for a in range(b+1):
            if (a**2 + b**2)==A:
                print(a, b)
                break
