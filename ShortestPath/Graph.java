
public class Graph {
    public Vertex[] vertices;
    public LinkedList[] edges;

    public int size;


    //Um nó pronto de uma lista ligada
    public class LinkedList {
        int weight = -1;
        int number = -1;
        LinkedList next = null;
    }

    //Nao tem fila de prioridade :(

    //Um vertice
    public class Vertex {
        boolean pass = false;
        int path;
        //Tinha q mudar
        int[] before = new int[size];
        int qBefore = 0;
    }

    public Graph(int vertices) {
        this.size = vertices;
        this.edges = new LinkedList[vertices];
        this.vertices = new Vertex[vertices];
        for (int i = 0; i < vertices; i++)  this.vertices[i] = new Vertex();
    }
    //Omega(c)
    public void pull(int vertex1, int vertex2, int weight) {
        LinkedList l = new LinkedList();
        l.weight = weight;  l.number = vertex2; l.next = this.edges[vertex1];
        this.edges[vertex1] = l;
    }
    //Omega(N)
    public void popEdge(Graph Graph, int vertex1, int vertex2) {
        LinkedList aresta = Graph.edges[vertex2];
        LinkedList aresta2 = Graph.edges[vertex2];
        while (aresta != null && aresta.number != vertex1) { aresta2 = aresta; aresta = aresta.next; }
        if (aresta == null) return;
        aresta2.next = aresta.next;
    }
    // Omega(N)
    public void setAll(int path) {
        for (int i = 0; i < this.size; i++) {
            this.vertices[i].path = path;
        }
    }
}