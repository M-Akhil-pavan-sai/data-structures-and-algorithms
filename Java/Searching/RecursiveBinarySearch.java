package Java.Searching;

import java.util.Scanner;

public class RecursiveBinarySearch {
    public static int BinarySearch(int arr[],int low, int high, int mid,int key)
    {
        if(low<=high)
        {
            if(arr[mid]==key)
            {
                return mid;
            }
            else if(arr[mid]>key)
            {
                return BinarySearch(arr, low, mid-1, low+(mid-1-low)/2, key);
            }
            else 
            {
                return BinarySearch(arr, mid+1, high, mid+1+(high-mid-1)/2, key);
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int arr[]=new int[5];

        System.out.println("Enter 5 elements of the array");
   

        for(int i=0;i<5;i++)
        {
            arr[i]=scanner.nextInt();
        }
        System.out.println("Enter key elements to search");
        int key = scanner.nextInt();
        int low=0;
        int high=arr.length-1;
        int mid = low+(high-low)/2;
        int result = BinarySearch(arr,low,high,mid,key);
        if(result==-1)
        {
            System.out.println("Element Not Found"+result);
        }
        else{
            System.out.println("Element Found at position"+result);
        }
        scanner.close();
    }
}
