class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


n, m = map(int, raw_input().split())
g = Graph()
for i in xrange(1, n+1):
    g.add_vertex(Vertex(str(i)))
edges = []
for i in xrange(m):
    edges.append(raw_input().replace(' ',''))
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

