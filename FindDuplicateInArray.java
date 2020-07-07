package com.vishwa;

import java.util.HashSet;
import java.util.Scanner;

public class FindDuplicateInArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        HashSet<Integer> unique = new HashSet<>();
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        for (int i = 0; i < N; i++) {
            if(unique.contains(A[i])){
                System.out.println(A[i]);
                break;
            }
            else {
                unique.add(A[i]);
            }
        }
    }
}
