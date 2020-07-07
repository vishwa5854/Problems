package com.vishwa;

public class Main {

    public static void main(String[] args) {
        int[] arr = new int[]{-4,3,3,5,5,5,8,9,10,10,10,10,10,15,15,20};
        System.out.println(BS(arr, 0, arr.length - 1, 10));
    }

    private static int BS(int[] arr, int low, int high, int K){
        int mid = (low + high)/2;;
        int ans = -1;
        while (K != arr[mid]){
            mid = (low + high)/2;
            if(K < arr[mid]){
                high = mid;

            }else {
                low = mid+1;
            }
            if(K == arr[mid]){
                ans = mid;
            }
        }  
        return ans;
    }
}
