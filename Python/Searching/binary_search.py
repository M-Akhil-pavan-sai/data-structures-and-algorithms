arr = input("enter elements of the array\n").strip(" ").split(" ")
key = input("\nenter key element to be found\n")
low=0
high=len(arr)-1
mid=low+(high-low)//2
flag=True
while(low<=high):
    if(arr[mid]==key):
        print("Element found at index ",mid)
        flag=False
        break
    elif (arr[mid]>key):
        high=mid-1
    else:
        low=mid+1
    mid=low+(high-low)//2
if flag:
    print("Element not Found")