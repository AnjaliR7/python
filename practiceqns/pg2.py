list1=[]
list2=[]
n=int(input("enter the limit:"))
print ("enter the elements:")
list1=[int(input())for i in range(n)]
print("smallest element is:",min(list1))
print("largest element is:",max(list1))
print("list after deleting duplicate numbers:",set(list1))
n=int(input("enter the limit:"))
print("enter the elements:")
list2=[int(input())for i in range(n)]
print("sum of list is",list1+list2)
