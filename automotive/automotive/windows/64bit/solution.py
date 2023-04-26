import heapq
import json
import os
import sys


INFTY = sys.maxsize

class Node:
    name = ""
    path_length = INFTY
    previous = None
    
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.path_length < other.path_length
    def set_path_length(self, new_length):
        self.path_length = new_length
    def set_previous(self, new_previous):
        self.previous = new_previous
    def get_path_length(self):
        return self.path_length
    def get_previous(self):
        return self.previous
    def get_name(self):
        return self.name


def dijkstra(starter_node_name, map, all_nodes):
    
    # Initialize nodes, collect them in priority queue "unvisited nodes", and create a dictionary with the nodes
    unvisited_nodes = []
    for node in map:
        new_node = Node(node)
        if node == starter_node_name:
            new_node.set_path_length(0)
        heapq.heappush(unvisited_nodes, new_node)
        all_nodes[new_node.get_name()] = new_node

    while len(unvisited_nodes) != 0:
        current_node = heapq.heappop(unvisited_nodes)
        for neighbour_node_name in map[current_node.get_name()]:
            neighbour_node = all_nodes[neighbour_node_name]
            
            # Length of edge between current node und its neighbour
            edge_length = map[current_node.get_name()][neighbour_node_name]["Time"]
            if current_node.get_path_length() + edge_length < neighbour_node.get_path_length():
                neighbour_node.set_previous(current_node)
                neighbour_node.set_path_length(current_node.get_path_length() + edge_length)
        heapq.heapify(unvisited_nodes)


def find_shortest_path(starter_node, target_node, shortest_path):
    '''Shortest path from target to start'''
    shortest_path.append(target_node.get_name())

    # Making sure that it stops if there's no path between target and start
    if target_node.get_previous() and starter_node.get_name() != target_node.get_name():
        find_shortest_path(starter_node, target_node.get_previous(), shortest_path)


if __name__ == "__main__":
    with open(r"taskOne.json") as json_data:
        map = json.load(json_data)

    starter_node_name = sys.argv[1]
    target_node_name = "D4"
    all_nodes = {}

    dijkstra(starter_node_name, map, all_nodes)

    shortest_path = []
    find_shortest_path(all_nodes[starter_node_name], all_nodes[target_node_name], shortest_path)
    shortest_path.reverse()
    try:
        sys.stdout.write(shortest_path[1])
    except:
        print("You are already at your target destination")


        