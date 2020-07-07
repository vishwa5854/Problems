package com.vishwa;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class HotelBookingsOtherMethod {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        ArrayList<Integer> arrive = new ArrayList<>();
        ArrayList<Integer> depart = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arrive.add(scanner.nextInt());
        }
        for (int i = 0; i < N; i++) {
            depart.add(scanner.nextInt());
        }
        System.out.println(solve(arrive, depart, K));
    }

    public static boolean solve(ArrayList<Integer> arrive, ArrayList<Integer> depart, int K) {
        boolean ans = true;
        Collections.sort(arrive);
        Collections.sort(depart);
        int I = 1;
        int J = 0;
        K -= 1;
        for (int i = 1; i < arrive.size(); i++) {
            if ((I < arrive.size()) && (J < arrive.size())) {
                if (arrive.get(I) <= depart.get(J)) {
                    if (K > 0) {
                        K -= 1;
                        I += 1;
                        J += 1;
                    } else {
                        if (kali(depart, arrive.get(I))) {
                            I += 1;
                        } else {
                            ans = false;
                            break;
                        }
                    }
                } else {
                    if (K > 0) {
                        K -= 1;
                        I += 1;
                        J += 1;
                    } else {
                        return false;
                    }
                }
            }
        }
        return ans;
    }

    private static boolean kali(ArrayList<Integer> depart, int time) {
        if (depart.get(0) <= time) {
            depart.remove(0);
            return true;
        }
        return false;
    }

    private static boolean kali1(ArrayList<Integer> depart, int time) {
        int low = 0;
        int high = depart.size();
        int mid;
        while (low <= high) {
            mid = (low + high) / 2;
            if (depart.get(mid) <= time) {
                depart.remove(depart.get(mid));
                return true;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
}
