arr = input("enter elements of the array\n").strip(" ").split(" ")
key = input("\nenter key element to be found\n")
print("\ngiven array is arr: ",arr)
flag=True
i=0
last = arr[-1]
arr[len(arr)-1]=key
while arr[i]!=key:
    i+=1
    break
if(i<len(arr)-1 or arr[len(arr)-1]==last):
    print("Element found")
else:
    print("Element not found!")