package Leetcode.Blind75.Easy;

// 21. Merge Two Sorted Lists
// Solved
// Easy
// Topics
// Companies
// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

 

// Example 1:


// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]
 

// Constraints:

// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.val <= 100
// Both list1 and list2 are sorted in non-decreasing order.


//solution - using basic intuition when we compare each value in both lists and add element to final list and move forward in that selected list
// since we should return a sorted list we will add element which is smaller while comparing to the final list

import java.util.List;



  public class MergeTwoSortedLists {
      int val;
      MergeTwoSortedLists next;
      MergeTwoSortedLists() {}
      MergeTwoSortedLists(int val) { this.val = val; }
      MergeTwoSortedLists(int val, MergeTwoSortedLists next) { this.val = val; this.next = next; }
  }
 
class Solution {
    public MergeTwoSortedLists mergeTwoLists(MergeTwoSortedLists list1, MergeTwoSortedLists list2) {
        MergeTwoSortedLists finalList;
        MergeTwoSortedLists startingNode;
        if(list1==null)
        {
            return list2;
        }
        if(list2==null)
        {
            return list1;
        }
        if(list1.val>list2.val)
            {
                finalList=list2;
                list2=list2.next;
            }
            else if(list1.val<list2.val)
            {
                finalList=list1;
                list1=list1.next;
            }
            else{
                finalList=list2;
                list2=list2.next;
            }
            startingNode=finalList;
        while(list1!=null && list2!=null)
        {
            if(list1.val>list2.val)
            {
                finalList.next=list2;
                finalList=finalList.next;
                list2=list2.next;
            }
            else if(list1.val<list2.val)
            {
                finalList.next=list1;
                finalList=finalList.next;
                list1=list1.next;
            }
            else{
                finalList.next=list2;
                finalList=finalList.next;
                list2=list2.next;
            }
        }
        while(list1!=null)
        {
            finalList.next=list1;
                finalList=finalList.next;
                list1=list1.next;
        }
        while(list2!=null)
        {
            finalList.next=list2;
                finalList=finalList.next;
                list2=list2.next;
        }
        return startingNode;
    }
}