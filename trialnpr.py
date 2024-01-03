def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
def npr(n,r):
	return(fact(n)/fact(n-r))
print("hello trial message")  
n=int(input("enter n:"))  
r=int(input("enter r:"))  
s=npr(n,r)
print(s)
