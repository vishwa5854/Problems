package com.vishwa;

import java.util.Arrays;
import java.util.Scanner;

public class RestoringThreeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[4];
        for (int i = 0; i < 4; i++) {
            arr[i] = scanner.nextInt();
        }
        Arrays.sort(arr);
        int B = (arr[1] - arr[0] + arr[2]) / 2;
        int A = (arr[1] - B);
        int C = arr[3] - (A + B);
        System.out.println(A + " " + B + " " +C);
    }
}
