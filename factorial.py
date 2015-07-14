def facto(n):
    total,i=0,0
    for i in range(n):
        total+=i
    return total

def inp():
    n=int(input("Enter the value of n\n"))
    ans=facto(n)
    print(ans,'is the answer')

inp()        

