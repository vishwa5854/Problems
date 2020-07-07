package com.vishwa;

import java.util.Scanner;

public class GameSquares {
    public static void main(String[] args) {
        int n=100001;
        boolean[] valid =new boolean[n];
        int[] square =new int[1001];
        valid[0]=false;
        for(int i=0;i<1001;i++)
            square[i]=i*i;
        for(int i=1;i<n;i++) {
            for(int j=1;square[j]<=i;j++) {
                valid[i]|=(!valid[i-square[j]]);
                if(valid[i])
                    break;
            }
        }
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            int x=sc.nextInt();
            if(valid[x])
                System.out.println("Win");
            else
                System.out.println("Lose");
        }
    }
}

