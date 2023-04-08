//Nome: André Miyazawa
//Nusp: 11796187
import java.util.Scanner;

public class ShortestPath {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            int vertices = sc.nextInt();
            int edges = sc.nextInt();
            if (vertices == 0 || edges == 0) return;
            int start = sc.nextInt();
            int end = sc.nextInt();
            ShortPath sp = new ShortPath();
            Graph graph = sp.init(sc, vertices, edges);
            int x = sp.shortestPath(graph, start, end);
            System.out.println(x);
        }
    }
}

class ShortPath{
    private static final int Infinity = 1000000;

    //Inicializa os valores no grafo
    public Graph init(Scanner sc, int vertices, int edges) {
        Graph graph = new Graph(vertices);
        for (int i = 0; i < edges; i++) graph.pull(sc.nextInt(), sc.nextInt(), sc.nextInt());
        return graph;
    }
    public Graph initUnweight(Scanner sc, int vertices, int edges) {
        Graph graph = new Graph(vertices);
        for (int i = 0; i < edges; i++) graph.pull(sc.nextInt(), sc.nextInt(), 1);
        return graph;
    }
    public Graph initDirected(Scanner sc, int vertices, int edges) {
        Graph graph = new Graph(vertices);
        for (int i = 0; i < edges; i++) {
            int v1 = sc.nextInt();  int v2 = sc.nextInt();  int p = sc.nextInt();

            graph.pull(v1, v2, p);
            graph.pull(v2, v1, p);
        }
        return graph;
    }
    /*
    Funcao para descobrir um quase menor caminho dado um grafo, o comeco do caminho
    E o seu fim
    */
    public int shortestPath(Graph Graph, int start, int end) {
        deaphFirstSearch(Graph, start, end);
        //breadthFirstSearch(Graph, start, end);
        //dijkstra(Graph, start, end);
        int path = Graph.vertices[end].path;
        if (path == Infinity) return -1;
        return path;
    }
    /*
    O algoritmo ultilizado foi o algoritmo de dijkstra
    Ele consiste em, dado um grafo e um conjunto de vertices gravados, deve:
    Gravar e selecionar a das somas das distancias do vertice v ( começo )
    e um outro vertice que o algoritmo nao gravou antes.
    Pegar a menor soma das distancias e gravar o vertice.
    Realizar até que nao haja mais vertices nao gravados.
    Omega(N) com N = V + A
     */
    protected void dijkstra(Graph graph, int start, int end) {
        graph.setAll(Infinity);
        Graph.LinkedList edge = graph.edges[start];
        if (edge == null)
            return;
        Graph.Vertex vertex = graph.vertices[start];
        int pont = start;
        vertex.path = 0;
        vertex.pass = true;
        for (int i = 0; i < graph.size; i++) {
            //Em um vertice:
            do {
                //Se nao possui arestas disponiveis com ninguem, sai do while
                if (edge == null) break;
                if (edge.weight == -1) break;
                /*
                Primeiro compara o weight do path escolhido mais o path percorrido anteriormente pelo vertice
                 e se ele for MENOR(1) ou IGUAL(2) que o path que ja existia até o determinado vertex ele:
                    (1): A quantidade de ponteiros para o anterior se torna 1 e o ponteiro Anterior do vertice se torna o pont
                    (2): A quantidade de ponteiros para o anterior é incrementada em 1 e é adicionado um que se torna o pont
                Para finalizar o programa atualiza o valor do path para o path mais curto.
                 */
                if (edge.weight + vertex.path <= graph.vertices[edge.number].path && !graph.vertices[edge.number].pass) {
                    if(edge.weight + vertex.path < graph.vertices[edge.number].path){
                        graph.vertices[edge.number].before[0] = pont;
                        graph.vertices[edge.number].qBefore = 1;
                    }
                    else {
                        graph.vertices[edge.number].before[graph.vertices[edge.number].qBefore] = pont;
                        graph.vertices[edge.number].qBefore++;
                    }
                    graph.vertices[edge.number].path = edge.weight + vertex.path;
                }
                //Vai para a proxima aresta
                edge = edge.next;
                //Se nao possui vertices disponiveis com ninguem, sai do while
            } while (edge != null);
            int index = -1;
            int minimal = Infinity;
            //Pega o menor path para seguir;
            //Verifica um por um qual é o menor caminho
            for (int j = 0; j < graph.vertices.length; j++) {
                if (minimal > graph.vertices[j].path && !graph.vertices[j].pass){
                    minimal = graph.vertices[j].path;
                    index = j;
                }
            }
            //Atualiza os ponteiros e cai no mesmo algoritmo com um vertice diferente
            pont = index;
            if (index == -1 || index == end) return;
            graph.vertices[index].pass = true;
            edge = graph.edges[index];
            vertex = graph.vertices[index];
        }
    }
    protected void setSecondLowPath(Graph graph, int pont) {
        Graph.LinkedList edge = graph.edges[pont];
        Graph.Vertex vertex = graph.vertices[pont];
        while (edge != null && edge.weight != -1) {
            Graph.LinkedList edgeNext = graph.edges[edge.number];
            Graph.Vertex vertexNext = graph.vertices[edge.number];
            while (edgeNext != null && edgeNext.weight != -1) {
                if (edgeNext.weight + edge.weight + vertex.path <= graph.vertices[edgeNext.number].path && !graph.vertices[edgeNext.number].pass) {
                    if (edgeNext.weight + edge.weight + vertex.path < graph.vertices[edgeNext.number].path) {
                        graph.vertices[edgeNext.number].before[0] = pont;
                        graph.vertices[edgeNext.number].qBefore = 1;
                    } else {
                        graph.vertices[edgeNext.number].before[graph.vertices[edgeNext.number].qBefore] = pont;
                        graph.vertices[edgeNext.number].qBefore++;
                    }
                    graph.vertices[edgeNext.number].path =edgeNext.weight + edge.weight + vertex.path;
                }
                edgeNext = edgeNext.next;
            }
            edge = edge.next;
        }
    }

    protected void deaphFirstSearch(Graph graph, int start, int end){
        graph.setAll(Infinity);
        graph.vertices[start].path = 0;
        DFSRec(graph, start, end);
    }
   protected void DFSRec(Graph graph, int start, int end){
        if (graph.edges[start] == null || start == end || graph.edges[start].number == -1)
            return;
        graph.vertices[start].pass = true;
        Graph.LinkedList edge = graph.edges[start];
        while (edge != null){
            if (graph.vertices[edge.number].pass) {
                edge = edge.next;
                continue;
            }
            if (edge.weight + graph.vertices[start].path < graph.vertices[edge.number].path && !graph.vertices[edge.number].pass) {
                graph.vertices[edge.number].before[0] = start;
                graph.vertices[edge.number].path = edge.weight + graph.vertices[start].path;
                DFSRec(graph, edge.number, end);
            }
            edge = edge.next;
        }
        graph.vertices[start].pass = false;
    }
    protected void breadthFirstSearch(Graph graph, int start, int end){
        /*
        ListaLigada lista
        vertice = primeiro elemento na lista
        while (elem na lista){
            ler todos vizinhos do vertice e gravar na lista
            vertice = vertice.next
            remove vertice
        }
         */
    }
    protected void TopoologicalSort(Graph graph, int start){
        
    }
}


