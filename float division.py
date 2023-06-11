#Float division between two integers
n=int(input("Enter an integer:"))
d=int(input("Enter another integer:"))
n//d==float(n/d)
d//n==float(d/n)
print(n,"//",d,"=",n//d)
print(d,"//",n,"=",d//n)
