arr = input("enter elements of the array\n").strip(" ").split(" ")
key = input("\nenter key element to be found\n")
print("\ngiven array is arr: ",arr)
flag=True
for i in range(len(arr)):
    if arr[i]==key:
        flag=False
        print("element found at position ",i+1)
        break
if flag:
    print("element not found!")