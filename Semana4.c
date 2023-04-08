#include <stdio.h>

int armadilha (int p1, int p2, int x, int y, char matrix[x][y]){
    if(matrix[p1 + 1][p2] == 'T')
        return 0;
    if(matrix[p1 - 1][p2] == 'T')
        return 0;
    if(matrix[p1][p2 + 1] == 'T')
        return 0;
    if(matrix[p1][p2 - 1] == 'T')
        return 0;
    return 1;
}
int esta_matrix(int p1, int p2, int x, int y ){
    if (p1 >= x || p1 < 0)
        return 0;
    if (p2 >= y || p2 < 0)
        return 0;
    return 1;
}
int jogo(int p1, int p2, int x, int y, char matrix[x][y]){
    int aux;
    int ouro = 0;
    if(!armadilha(p1, p2, x, y, matrix))
        return 0;
    for (int i = 1, j = 0; i >= -1 ; i = i -2) {
        if (matrix[p1 + i][p2 + j] != '#' && matrix[p1 + i][p2 + j] != 'P') {
            if (esta_matrix(p1 + i, p2 + j, x, y)) {
                if (matrix[p1 + i][p2 + j] == 'G')
                    ouro++;
                matrix[p1 + i][p2 + j] = '#';
                ouro = ouro + jogo(p1 + i, p2 + j, x, y, matrix);
            }
        }
    }
    for (int j = 1, i = 0; j >= -1 ; j = j -2) {
        if (matrix[p1 + i][p2 + j] != '#' && matrix[p1 + i][p2 + j] != 'P') {
            if (esta_matrix(p1 + i, p2 + j, x, y)) {
                if (matrix[p1 + i][p2 + j] == 'G')
                    ouro++;
                matrix[p1 + i][p2 + j] = '#';
                ouro = ouro + jogo(p1 + i, p2 + j, x, y, matrix);
            }
        }
    }

    return ouro;
}
int main() {
    int x, y;
    scanf("%i %i", &y, &x);
    if(x < 3 || x > 50 || y < 3 || y > 50)
        return 0;
    int p1, p2;
    char matrix[x][y];
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            matrix[i][j] = fgetc(stdin);
            while (matrix[i][j] == 10)
                matrix[i][j] = fgetc(stdin);
            if (matrix[i][j] == 'P') {
                p1 = i;
                p2 = j;
            }
        }
    }
    int ouro = jogo(p1, p2, x, y, matrix);
    printf("%i\n", ouro);
}