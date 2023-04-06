//André Miyazawa - 11796187

import java.util.Scanner;
public class Bombs_NO_they_are_Mines {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int[] dim = {sc.nextInt(), sc.nextInt()};
            if (dim[0] == 0 && dim[1] == 0)
                return;
            int nbombs = sc.nextInt();

            if(nbombs == 0){
                int[] start = {sc.nextInt(), sc.nextInt()};
                int[] end = {sc.nextInt(), sc.nextInt()};
                System.out.println(Math.abs(start[0] - end[0]) + Math.abs(start[1] - end[1]));
                continue;
            }
            Casa[][] m = new Casa[dim[0]][dim[1]];
            for (int i = 0; i < dim[0]; i++) for (int j = 0; j < dim[1]; j++) m[i][j] = new Casa(false, null);

            for (int i = 0; i < nbombs; i ++){
                int line = sc.nextInt();
                int ncols = sc.nextInt();
                for (int j = 0; j < ncols; j++) {
                    int col = sc.nextInt();
                    m[line][col].visited = true;
                    m[line][col].pais = null;
                }
            }
            int[] start = {sc.nextInt(), sc.nextInt()};
            int[] end = {sc.nextInt(), sc.nextInt()};
            dfs(m, dim, start);
            System.out.println(menor_distancia(m, start, end));
        }
    }
    static void dfs(Casa[][] m,int[] dim,int[] start){
        int [][] vec = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };
        int inf = dim[0] * dim[1];

        int[] atual;
        int[][] nexts = new int[inf][];
        int index = 1;
        int indexRem = 0;
        nexts[0] = start;
        m[start[0]][start[1]].visited = true;

        while (index != indexRem){
            atual = nexts[indexRem];
            nexts[indexRem] = null;
            indexRem++;

            for (int i = 0; i < 4; i++) {
                int[] check = {atual[0] + vec[i][0], atual[1] + vec[i][1]};
                if (
                        ((0 <= check[0] && check[0] < dim[0]) && (0 <= check[1] && check[1] < dim[1]))
                        && !(m[check[0]][check[1]].visited)
                ) {
                    m[check[0]][check[1]].visited = true;
                    m[check[0]][check[1]].pais = new int[]{atual[0], atual[1]};
                    nexts[index] = new int[]{check[0], check[1]};
                    index++;
                }
            }
        }
    }

    static int menor_distancia(Casa[][] m, int[]start, int [] end){
        int path = 0;
        while (start[0] != end[0] || start[1] != end[1]){
            end = m[end[0]][end[1]].pais;
            path++;
        }
        return path;
    }

}


class Casa{
    boolean visited;
    int[] pais;

    public Casa(boolean visited, int[] pais) {
        this.visited = visited;
        this.pais = pais;
    }
}
