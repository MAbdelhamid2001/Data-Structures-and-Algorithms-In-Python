class graph: #unweighted graph
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.output = []

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    # def get_paths(self,start,end,path=[]):

    #     #mumbai,newyork
    #     path = path+[start]

    #     if start == end:
    #         self.output.append(path)
    #         return

    #     if start not in self.graph_dict:
    #         return []
    #     # print(self.graph_dict[start])

    #     for i in self.graph_dict[start]:
    #         if i not in path:
    #             self.get_paths(i,end,path)

    def get_paths(self, start, end, path=[]):

        # mumbai,newyork
        path = path+[start]

        if start == end:
            # self.output.append(path)
            return [path]

        if start not in self.graph_dict:
            return []
        # print(self.graph_dict[start])

        paths = []
        for i in self.graph_dict[start]:
            if i not in path:
                new_paths = self.get_paths(i, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):#dfs for unweighted graph
        path = path+[start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        shortest_path = None
        for i in self.graph_dict[start]:
            if i not in path:
                new_path = self.get_shortest_path(i, end, path)

                if new_path:
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        shortest_path = new_path

        return shortest_path

if __name__ == '__main__':

    routes = [

        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'NewYork'),
        ('Dubai', 'NewYork'),
        ('NewYork', 'Toronto')
    ]

    route_graph = graph(routes)

    # print(route_graph.graph_dict['Mumbai'])

    # route_graph.get_paths('Paris','NewYork')
    # print(route_graph.output)

    # print(route_graph.get_paths('Mumbai','NewYork'))
    print(route_graph.get_shortest_path('Mumbai', 'NewYork'))







