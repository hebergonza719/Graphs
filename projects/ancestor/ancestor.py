class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



def get_parents(node, ancestors):
    parent = []

    for x in ancestors:
        if x[1] == node:
            parent.append(x[0])
    return parent    



def earliest_ancestor(ancestors, starting_node):
    # pass
    if starting_node < 0:
        return -1

    if len(get_parents(starting_node, ancestors)) == 0:
        return -1

    q = Queue()

    visited = set()

    max_path = [starting_node]

    q.enqueue([starting_node])

    while q.size() > 0:

        current_path = q.dequeue()

        current_node = current_path[-1]

        parents = get_parents(current_node, ancestors)
        
        if current_node not in visited:
            visited.add(current_node)
        
            for parent in parents:
                path_copy = list(current_path)
                path_copy.append(parent)
                q.enqueue(path_copy)

                if max_path is path_copy:
                    pass
                elif len(max_path) < len(path_copy):
                    max_path = path_copy
                elif len(max_path) == len(path_copy):
                    if max_path[-1] > path_copy[-1]:
                        max_path = path_copy
    
    return max_path[-1]
                
        




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))