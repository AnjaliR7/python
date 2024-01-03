def fact(n):
  if n==1:
   return 1
  else:
   return n*fact(n-1)
def npr(n,r):
   return(fact(n)/fact(n-r))
print("trial message")    
n,r=input("enter n &r").split()
print(n,"p", r, " : ",npr(int(n),int(r)) 
