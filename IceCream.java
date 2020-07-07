package com.vishwa;

import java.util.Scanner;

public class IceCream {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int z = 0; z < T; z++) {
            int N = scanner.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
            String ans = "YES";
            int five = 0;
            int ten = 0;
            for (int i = 0; i < N; i++) {
                if(arr[i] == 5){
                    five += 1;
                }
                else if(arr[i] == 10){
                    if(five >  0) {
                        five -= 1;
                        ten += 1;
                    }
                    else {
                        ans = "NO";
                        break;
                    }
                }
                else {
                    if(ten > 0) {
                        ten -= 1;
                    }
                    else if(five >= 2){
                        five -= 2;
                    }
                    else {
                        ans = "NO";
                        break;
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
