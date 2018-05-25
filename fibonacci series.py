x=int(input("Enter the first number of the series "))
y=int(input("Enter the second number of the series "))
N=int(input("Enter the number of terms needed "))
print(x,y,end=" ")
while(N-2):
    z=x+y
    x=y
    y=z
    print(z,end=" ")
    N=N-1
