package com.vishwa;

import java.util.Scanner;

public class ILoveUserName {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int count = 0;
        int max = -1;
        int min = (int) 1e9;
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = scanner.nextInt();
        }
        if(n >= 2){
            if(scores[0] > scores[1]){
                max = scores[0];
                min = scores[1];
            }
            else {
                max = scores[1];
                min = scores[0];
            }
        }
        else {
            count = -1;
        }
        for (int i = 2; i < n; i++) {
            if(scores[i] > max){
                max = scores[i];
                count += 1;
            }
            else if(scores[i] < min){
                min = scores[i];
                count += 1;
            }
        }
        System.out.println(count + 1);
    }
}
