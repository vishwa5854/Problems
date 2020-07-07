package com.vishwa;

import java.util.*;

public class FarewellParty {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int z = 0; z < t; z++) {
            int n = scanner.nextInt();
            SortedMap<Integer, Integer> s = new TreeMap<>();
            ArrayList<Integer> arrival = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int a = scanner.nextInt();
                int d = scanner.nextInt();
                arrival.add(a);
                s.put(a, d);
            }
            Collections.sort(arrival);
            int I = 1;
            int J = 0;
            int K = 1;
            for (int i = 0; i < n; i++) {
                if((I < n) && (J < n)){
                    if(arrival.get(I) <= s.get(arrival.get(J))){
                        if(kali(s, arrival.get(I))){
                            arrival.remove(0);
                        }
                        else {
                            K += 1;
                            I += 1;
                            J += 1;
                        }
                    }
                }
            }
            System.out.println(K);
        }
    }

    private static boolean kali(SortedMap<Integer, Integer> sd, int time) {
        if (sd.get(sd.firstKey()) <= time) {
            sd.remove(sd.firstKey(), sd.firstKey());
            return true;
        }
        return false;
    }
}
