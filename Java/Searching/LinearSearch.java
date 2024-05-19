package Java.Searching;
import java.util.Scanner;

public class LinearSearch
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        int arr[]=new int[5];

        System.out.println("Enter 5 elements of the array");
   

        for(int i=0;i<5;i++)
        {
            arr[i]=scanner.nextInt();
        }
        System.out.println("Enter key elements to search");
        int key = scanner.nextInt();
        boolean flag=true;
        for(int i:arr)
        {
            if(i==key)
            {
                flag=false;
                System.out.println("Element Found");

            }
        }
        if(flag)
        {
            System.out.println("Element Not Found");

        }
        scanner.close();
    }
}