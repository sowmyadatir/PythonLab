def primeGen(m,n):
    for i in range(m, n+1):
        if i == 2:
            print(i, end=" ")
        if i>2:
            for j in range(2,i//2 + 2):
                if i%j == 0:
                    break
                else:
                    if j == i//2 + 1:
                        print(i, end=" ")
                           
           
t=int(input("Enter the number of test cases: "))
for i in range(t):
        m, n = input("Enter two numbers: ").split()
        primeGen(int(m), int(n))
