package com.vishwa;

import java.util.HashMap;

public class LearnStrings {
    public static void main(String[] args) {
        String a = "kashi vishwanath";
        System.out.println(a.hashCode());
        HashMap<String, String> hm = new HashMap<>();
        hm.put("a","b");
        hm.put("b","b");
        hm.put("c","b");
        hm.put("d","b");
        System.out.println(hm.containsKey("d"));
        System.out.println(hm.containsKey("e"));
    }
}
