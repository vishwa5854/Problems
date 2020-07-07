package com.vishwa;

import java.util.Scanner;

public class Chef {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int T  = scanner.nextInt();
        for(int z = 0; z < T ; z ++){
            String a = scanner.next();
            int n = a.length();
            int ans = 0;
            for (int i = 0; i < n - 1; i++) {
                if(a.charAt(i) == 'x'){
                    if(a.charAt(i + 1) == 'y'){
                        ans += 1;
                        i += 1;
                    }
                }
                else if(a.charAt(i) == 'y'){
                    if(a.charAt(i + 1) == 'x'){
                        ans += 1;
                        i += 1;
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
