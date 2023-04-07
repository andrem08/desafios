import java.util.*;
//Problema 1193
//André Miyazawa

public class Testing_the_CATCHER {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = null;
        int count = 1;
        int n;
        while (true){
            n = sc.nextInt();
            if(n == -1) break;
            if (count > 1)
                System.out.printf("\n");
            arr = new ArrayList<Integer>();
            arr.add(n);

            while (true) {
                n = sc.nextInt();
                if(n == -1) break;
                arr.add(n);
            }
            int size = arr.size();
            int []d = new int[size];
            for (int i = 0; i < size; i++) d[i] = 1;
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < i; j++) {
                    if (arr.get(j) >= arr.get(i))
                        d[i] = Math.max(d[i], d[j] + 1);
                }
            }
            int res = d[0];
            for (int i = 1; i < size; i++) {
                res = Math.max(res, d[i]);
            }
            System.out.println("Test #"+count+":");
            System.out.println("  maximum possible interceptions: "+res);
            count++;
        }
    }
}
