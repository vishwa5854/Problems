package com.vishwa;

import java.util.Scanner;
import java.util.SortedMap;
import java.util.TreeMap;

public class WindowMaximum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int z = 0; z < T; z++) {
            int N = scanner.nextInt();
            int K = scanner.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
            SortedMap<Integer, Integer> map = new TreeMap<>();
            for (int i = 0; i < K; i++) {
                map.put(arr[i], i);
            }
            int s = map.lastKey();
            for (int i = 0; i < N - K; i++) {
                map.remove(arr[i]);
                map.put(arr[i + K], i + K);
                s += map.lastKey();
            }
            System.out.println(s);
        }
    }
}
