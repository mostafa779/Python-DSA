class Graph:

    def __init__(self,graph = {}):
        self.__graph = graph 

    def vertices(self):
        return list(self.__graph.keys())

    def edges(self):
        return self.__generate_edges()

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph:
            for neighbour in self.__graph[vertex]:
                if {vertex,neighbour} not in edges:
                    edges.append({vertex,neighbour})
        return edges

    def add_vetex(self,vertex):
        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def add_edge(self,edge):
        edge = set(edge)
        (v1,v2) = tuple(edge)
        if v1 in self.__graph:
            self.__graph[v1].append(v2)
        else:
            self.__graph[v1] = v2

    def __str__(self):
        o = "Vertices: "
        for v in self.__graph:
            o += str(v)+' '
        o += "\nEdges: "
        for e in self.__generate_edges():
            o += str(e)+' '
        return o

    def find_path(self, start, end, path = []):
        if start not in self.__graph:
            return None
        path += [start]
        if start == end:
            return path
        for vertex in self.__graph[start]:
            if vertex not in path:
                sub_path = self.find_path(vertex,end,path)
                if sub_path is not None:
                    return sub_path
        return None

    def find_all_paths(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.__graph:
            return []
        paths = []
        for vertex in self.__graph[start]:
            if vertex not in path:
                sub_paths = self.find_all_paths(vertex,end,path)
                for p in sub_paths:
                    paths.append(p)
        return paths

    def vertex_dgree(self,vertex):
        adj_vertices = self.__graph[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree



g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }
graph = Graph(g)

path = graph.find_all_paths("a", "e")
print(path)
# print(graph.vertex_dgree('d'))