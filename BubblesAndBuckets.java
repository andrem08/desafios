//André e Ailson

import java.util.*;

public class BubblesAndBuckets {

    public static int mergeSort(int[] a) {
        int n = a.length;

        if (n < 2) return 0;
        int trocas = 0;
        int mid = n / 2;
        int[] l = new int[mid];
        int[] r = new int[n - mid];

        System.arraycopy(a, 0, l, 0, mid);
        System.arraycopy(a, mid, r, 0, n - mid);

        trocas += mergeSort(l);
        trocas += mergeSort(r);

        return merge(a, l, r) + trocas;
    }
    public static int merge(int[] a, int[] l, int[] r) {
        int left = l.length;
        int right = r.length;
        int li = 0, ri = 0, i = 0, trocas = 0;
        while (li < left && ri < right)
            if (l[li] <= r[ri]) a[i++] = l[li++];
            else {
                a[i++] = r[ri++];
                trocas += (l.length - li);
            }
        while (li < left)
            a[i++] = l[li++];
        while (ri < right)
            a[i++] = r[ri++];
        return trocas;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n == 0)
                break;
            int[] numero = new int[n];
            for (int i = 0; i < n; i++)
                numero[i] = sc.nextInt();

            int trocas = mergeSort(numero);
            if (trocas % 2 == 1) System.out.println("Marcelo");
            else System.out.println("Carlos");
        }
    }
}
