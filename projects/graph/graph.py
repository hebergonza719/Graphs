"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if type(v1) == str:
            print("Please use numbers")
            return
        else:
            self.vertices[v1].add(v2)
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            current_node = q.dequeue()

            if current_node in visited:
                pass
            else:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for i in neighbors:
                    q.enqueue(i)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()

            if current_node in visited:
                pass
            else:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for i in neighbors:
                    s.push(i)

        


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = []

        def helper(starting_node, visited_list):
            visited_list.append(starting_node)
            print(starting_node)

            for neighbor in self.vertices[starting_node]:
                if neighbor not in visited_list:
                    visited_list = helper(neighbor, visited_list)
            
            return visited_list

        visited = helper(starting_vertex, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = []

        q = Queue()

        first_path = [starting_vertex]

        q.enqueue(first_path)

        if starting_vertex in self.vertices and starting_vertex == destination_vertex:
            visited.append(starting_vertex)
            return visited

        else: 
            while q.size() > 0:
                path = q.dequeue()
                node = path[-1]
                if node not in visited:
                    neighbors = self.get_neighbors(node)
                    for neighbor in neighbors:
                        # get old path and store it in new_path
                        new_path = list(path)
                        # add new neighbors to new_path
                        new_path.append(neighbor)
                        # add new_path to the queue
                        q.enqueue(new_path)
                        # if the neighbor that was just added is the destination,
                        # return the new_path created in this cycle
                        if neighbor == destination_vertex:
                            return new_path
                    # add node into visited list
                    visited.append(node)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
    # print(graph.vertices)
    
#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
    # graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
    # graph.dft(1)
    # graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
    print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))
