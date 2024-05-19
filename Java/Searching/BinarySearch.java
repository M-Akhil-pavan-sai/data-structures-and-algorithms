package Java.Searching;

import java.util.Scanner;

public class BinarySearch {
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
        boolean flag= true;
        while(low<=high)
        {
            if(key==arr[mid])
            {
                System.out.println("Element Found at index : "+mid);
                flag=false;
                break;
            }
            else if(arr[mid]>key)
            {
                high=mid-1;
                
            }
            else if(arr[mid]<key)
            {
                low=mid+1;
            }
            mid = low+(high-low)/2;
        }
        if(flag)
        {
            System.out.println("Element Not Found");
        }
        scanner.close();
    }
}
