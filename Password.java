//UVA 1262

import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

import static java.util.Arrays.*;

public class Password {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int order = sc.nextInt();
            char [][]m1 = new char[5][6];
            char [][]m2 = new char[5][6];
            sc.nextLine();
            String next;
            //O(n)
            for (int j = 0; j < 6; j++) {
                next = sc.next();
                for (int k = 0; k < 5; k++)
                    m1[k][j] = next.charAt(k);
            }
            for (int j = 0; j < 6; j++) {
                next = sc.next();
                for (int k = 0; k < 5; k++)
                    m2[k][j] = next.charAt(k);
            }
            //Ordena em ordem crescente as duas matrizes
            //O(n*log(n))
            for (int j = 0; j < 5; j++) {
                sort(m1[j]);
                sort(m2[j]);
            }
            int[] count = {0};
            char[] password = new char[5];
            getPassword(m1, m2, password, 0, count, order);
            //Se o contador for igual ao limite, imprime a senha, caso contrário imprime NO
            if (count[0] == order) System.out.println(password);
            else System.out.println("NO");
        }
    }

    //Função recursiva que simula 5 for's
    static void getPassword(char[][] m1, char[][] m2, char[] password, int n, int[]count, int order){
        if (n == 5) {
            //Verifica a existência da senha na matriz m2, se existe o contador soma 1
            //O(log(n))
            if (binarySearch(m2[0], password[0]) >= 0 && binarySearch(m2[1], password[1]) >= 0 && binarySearch(m2[2],
                    password[2]) >= 0 && binarySearch(m2[3], password[3]) >= 0 && binarySearch(m2[4], password[4]) >= 0)
                count[0]++;
            return;
        }

        //Simulando as 5 iterações deste for, no pior caso são 5^6 = 15.625
        for (int i = 0; i < 6; i++) {
            //Caso o elemento seja repetido
            if (i > 0 && Objects.equals(m1[n][i], m1[n][i - 1]))
                continue;
            password[n] = m1[n][i];
            getPassword(m1, m2, password, n + 1, count, order);
            //Se o contador for igual ao limite, sai da função.
            if (count[0] == order) break;
        }
    }
}
