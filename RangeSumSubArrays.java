package com.vishwa;

import java.util.Scanner;

public class RangeSumSubArrays {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int z = 0; z < t; z++) {
            int N = scanner.nextInt();
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            int ans = 0;
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
            for (int i = 0; i < N; i++) {
                for (int j = i; j < N; j++) {
                    int s = 0;
                    for (int k = i; k <= j; k++) {
                        s += arr[k];
                    }
                    if((A <= s) && (s <= B)){
                        ans += 1;
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
