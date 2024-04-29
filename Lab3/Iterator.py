from collections import deque


class IteratorBFS:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.visited = set()
        self.queue = deque()
        self.queue.append(start_vertex)
        self.current = None
        self.distances = {start_vertex: 0}

    def first(self):
        self.current = self.start_vertex
        return self.current

    def get_current(self):
        if self.valid():
            return self.current
        else:
            raise ValueError("Iterator is invalid")

    def next(self):
        if not self.valid():
            raise ValueError("Iterator is invalid")

        if self.queue:
            self.current = self.queue.popleft()
            for neighbor in self.graph.adj_list.get(self.current, []):
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.distances[neighbor] = self.distances[self.current] + 1
            return self.current
        else:
            self.current = None
            raise ValueError()

    def valid(self):
        return self.current is not None

    def get_path_length(self):
        if self.valid():
            return self.distances.get(self.current, 0)
        else:
            raise ValueError("Iterator is invalid")

