package com.vishwa;

import java.util.*;

public class HotelBookingsPossible {
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
        boolean answer = true;
        Collections.sort(arrive);
        Collections.sort(depart);
        int[] hotel = new int[K];
        for (int i = 0; i < N; i++) {
            int room = vacancy(hotel, K);
            if(room >= 0){
                hotel[room] = depart.get(i);
            }
            else {
                room = remove(hotel, K, arrive.get(i));
                if(room >= 0){
                    hotel[room] = depart.get(i);
                }
                else {
                    answer = false;
                    break;
                }
            }
        }
        System.out.println(answer);
    }

    private static int vacancy(int[] hotel, int K){
        Arrays.sort(hotel);
        int low = 0;
        int high = K - 1;
        int mid;
        while (low <= high){
            mid = (low + high) / 2;
            if(hotel[mid] == 0){
                return mid;
            }
            else if(hotel[mid] > 0){
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }

    private static int remove(int[] hotel, int K, int time){
        int low = 0;
        int high = K - 1;
        int mid;
        while (low <= high){
            mid = (low + high) / 2;
            if(hotel[mid] <= time){
                hotel[mid] = 0;
                return mid;
            }
            else {
                high = mid - 1;
            }
        }
        return -1;
    }

}