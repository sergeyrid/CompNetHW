import json


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.routing_table = {self.name: {self.name: 0}}

    def set_neighbors(self, neighbors, weights):
        self.neighbors = neighbors
        for neighbor, weight in weights:
            self.routing_table[self.name][neighbor] = weight
            self.routing_table[neighbor] = {self.name: weight}
            for neighbor2, weight2 in weights:
                self.routing_table[neighbor][neighbor2] = -1

    def update_neighbor(self, neighbor, neighbor_vector):
        if neighbor not in map(lambda node: node.name, self.neighbors):
            return
        print(f'Node {self.name} receiving info from node {neighbor}')
        self.routing_table[neighbor] = neighbor_vector
        changed = False
        if neighbor_vector[self.name] < self.routing_table[self.name][neighbor]:
            self.routing_table[self.name][neighbor] = neighbor_vector[self.name]
            changed = True
        neighbor_distance = self.routing_table[self.name][neighbor]
        for neighbor2, weight2 in neighbor_vector.items():
            new_distance = neighbor_distance + weight2
            if neighbor2 not in self.routing_table[self.name] or \
                    new_distance < self.routing_table[self.name][neighbor2] or \
                    self.routing_table[self.name][neighbor2] == -1:
                self.routing_table[self.name][neighbor2] = new_distance
                changed = True
        if changed:
            self.send_info()

    def send_info(self):
        vector = self.get_vector()
        for neighbor in self.neighbors:
            print(f'Node {self.name} sending info to node {neighbor.name}')
            neighbor.update_neighbor(self.name, vector)

    def get_vector(self):
        return self.routing_table[self.name]

    def __repr__(self):
        return str(self.name)


def main():
    with open('input.json', 'r') as f:
        data = json.load(f)
    network = [Node(int(name)) for name in data]
    for node in network:
        weights = data[str(node.name)]
        neighbor_names = list(zip(*weights))[0]
        neighbors = list(filter(lambda neighbor: neighbor.name in neighbor_names, network))
        node.set_neighbors(neighbors, weights)

    print()
    print('Initial network:')
    print('--------------------------')
    for node in network:
        print(node, node.get_vector())
    print('--------------------------')
    print()

    for node in network:
        node.send_info()

    print()
    print('Final network:')
    print('--------------------------')
    for node in network:
        print(node, node.get_vector())
    print('--------------------------')
    print()


if __name__ == '__main__':
    main()
