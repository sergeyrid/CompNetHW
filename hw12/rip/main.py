import json


class Node:
    INF = 16

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.routing_table = {self.name: {self.name: 0}}
        self.paths = dict()
        self.iteration = 0

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
        neighbor_names = list(map(lambda node: node.name, self.neighbors))
        for neighbor in neighbor_names:
            self.routing_table[self.name][neighbor] = 1
            self.routing_table[neighbor] = {self.name: 1}
            self.paths[neighbor] = [neighbor]
            for neighbor2 in neighbor_names:
                self.routing_table[neighbor][neighbor2] = self.INF
        self.print_statistics()

    def update_neighbor(self, neighbor, neighbor_vector, neighbor_paths):
        if neighbor not in map(lambda node: node.name, self.neighbors):
            return
        self.routing_table[neighbor] = neighbor_vector
        changed = False
        for neighbor2, weight2 in neighbor_vector.items():
            new_distance = weight2 + 1
            if neighbor2 not in self.routing_table[self.name] or \
                    new_distance < self.routing_table[self.name][neighbor2] or \
                    self.routing_table[self.name][neighbor2] == self.INF:
                self.paths[neighbor2] = [neighbor] + neighbor_paths[neighbor2]
                self.routing_table[self.name][neighbor2] = new_distance
                changed = True
        if changed:
            self.iteration += 1
            self.print_statistics()
            self.send_info()

    def send_info(self):
        vector = self.get_vector()
        for neighbor in self.neighbors:
            neighbor.update_neighbor(self.name, vector,  self.paths)

    def print_statistics(self):
        print(f'Simulation step {self.iteration} of router {self.name}')
        print('[Source IP]      [Destination IP]      [Next Hop]      [Metric]')
        for node, path in self.paths.items():
            print(f'{self.name:<15}  {node:<15}       {path[0]:<15}       {len(path):>2}')
        print()

    def print_final_statistics(self):
        print(f'Final state of router {self.name} table:')
        print('[Source IP]      [Destination IP]      [Next Hop]      [Metric]')
        for node, path in self.paths.items():
            print(f'{self.name:<15}  {node:<15}       {path[0]:<15}       {len(path):>2}')
        print()

    def get_vector(self):
        return self.routing_table[self.name]

    def __repr__(self):
        return self.name


def main():
    with open('input.json', 'r') as f:
        data = json.load(f)
    network = [Node(name) for name in data]
    for node in network:
        neighbors = list(filter(lambda neighbor: neighbor.name in data[node.name], network))
        node.set_neighbors(neighbors)

    for node in network:
        node.send_info()

    for node in network:
        node.print_final_statistics()


if __name__ == '__main__':
    main()
