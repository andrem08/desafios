import java.util.*;
//Problema 1193
//André Miyazawa, Ailton Domingues
//Para compilar no UVA, mudar o nome da classe para Main

public class RadarInstallation{
    public static void main(String[] args){
        //Variáveis
        Scanner sc = new Scanner(System.in);
        int cases = 1;
        int N, D;
        int[] x, y;
        double esquerda, direita;
        Tupla[] raios;
        boolean erro;

        while(true) {
            N = sc.nextInt();
            D = sc.nextInt();
            erro = false;
            if(N == 0 & D == 0) break;
            x = new int[N];
            y = new int[N];
            raios = new Tupla[N];
            System.out.print("Case "+cases+++": ");
            //Armazena as ilhas
            for (int i = 0; i < N; i++) {
                x[i] = sc.nextInt();
                y[i] = sc.nextInt();
                //Caso direita > D, é impossivel o radar encontrar
                if(y[i] > D)
                    erro = true;
            }
            sc.nextLine();
            // Caso tenha ocorrido o erro
            if (erro){
                System.out.println(-1);
                continue;
            }
            //Vamos achar os 2 possiveis radares mais longes de cada uma das coordenadas utilizando o teorema de Pitagoras
            for (int i = 0; i < N; i++) {
                double sqrt = Math.sqrt(Math.pow(D, 2) - Math.pow(y[i], 2));
                esquerda = x[i] - sqrt;
                direita = x[i] + sqrt;
                raios[i] = new Tupla(esquerda,direita);
            }
            //Ordenar pelo eixo esquerda, do menor para o maior
            Arrays.sort(raios);
            int nRadares = 0;
            int i = 0;
            while (i < raios.length) {
                double segundo_raio = raios[i].direita;
                for(; i < N ; i++) {
                    if(raios[i].esquerda > segundo_raio) break;
                    //Caso o raio mais a direita não seja o atual utilizado.
                    segundo_raio = Math.min(segundo_raio, raios[i].direita);
                }
                nRadares++;
            }
            System.out.println(nRadares);
        }
    }
    static class Tupla implements Comparable<Tupla> {
        double esquerda, direita;
        public Tupla(double esquerda, double direita) {
            this.esquerda = esquerda;
            this.direita = direita;

        }
        public int compareTo(Tupla objeto) {
            if(Double.compare(this.esquerda,objeto.esquerda) != 0)
                return Double.compare(this.esquerda,objeto.esquerda);
            return Double.compare(objeto.direita, this.direita);
        }
    }
}
