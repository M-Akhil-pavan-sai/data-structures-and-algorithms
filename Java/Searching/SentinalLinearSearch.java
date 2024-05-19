package Java.Searching;

import java.util.Scanner;

public class SentinalLinearSearch {
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
        int last = arr[arr.length-1];
        arr[arr.length-1]=key;
        int i=0;
        while(arr[i]!=key)
        {
            i++;
        }
        if(i<arr.length-1 || arr[arr.length-1]==last)
        {
            System.out.println("Element Found");
        }
        else{
            System.out.println("Element Not Found");
        }
        scanner.close();
    }
}

// number of comparision required for checking whether reached end of the array or not 
// is reduced in sentinal linear search there by increasing performance in average case
