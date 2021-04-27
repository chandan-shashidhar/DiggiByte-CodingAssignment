def countWays(n) :
    temp = [0] * (n + 2)
    temp[0] = 1
    temp[1] = 1
    temp[2] = 2
     
    for i in range(3, n + 1) :
        temp[i] = temp[i - 1] + temp[i - 2] + temp[i - 3]
     
    return temp[n]


print(countWays(int(input("Enter Number of steps : "))))


 