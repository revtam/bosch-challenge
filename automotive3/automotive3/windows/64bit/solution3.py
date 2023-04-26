import heapq
import json
import os
import sys


INFTY = sys.maxsize

class Node:
    name = ""
    path_length = INFTY
    previous = None
    light_status_counter = 0

    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.path_length < other.path_length
    def set_light_status_counter(self, new_counter_value):
        self.light_status_counter = new_counter_value % 2
    def get_light_status_counter(self):
        return self.light_status_counter
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


def dijkstra(starter_node_name, map, all_nodes, light_status_is_normal, starter_current_data):
    
    # Initialize nodes, collect them in priority queue "unvisited nodes", and create a dictionary with the nodes
    unvisited_nodes = []
    for node_name in map:
        new_node = Node(node_name)
        if node_name == starter_node_name:
            new_node.set_path_length(0)
            if not light_status_is_normal:
                new_node.set_light_status_counter(1)
        heapq.heappush(unvisited_nodes, new_node)
        all_nodes[new_node.get_name()] = new_node

    # The first node popped from the heap is always the starter node  
    is_starter_node = True
    while len(unvisited_nodes) != 0:
        current_node = heapq.heappop(unvisited_nodes)
        for neighbour_node_name in map[current_node.get_name()]:
            neighbour_node = all_nodes[neighbour_node_name]
            neighbour_node_data = map[current_node.get_name()][neighbour_node_name]

            # Length of edge between current node und its neighbour
            edge_length = neighbour_node_data["Time"]

            # Update light status of neightbour node depending on the light status of the current node
            light_status = neighbour_node_data["TrafficLight"]
            if current_node.get_light_status_counter():     # If its 1, the light has to be changed
                if light_status == 1:
                    light_status = 0
                if light_status == 0:
                    light_status = 1

            # If the light is red, the waiting time is added to the length of the edge
            if light_status == 0:
                edge_length += neighbour_node_data["TrafficLightDelay"]

            # When calculating the length of the edge, the potential length of traffic jam is 
            # estimated by the traffic jam delay multiplied by its probability of occurrence
            if is_starter_node:
                try:
                    traffic_jam_chance = starter_current_data[neighbour_node_name]["TrafficJam"]
                except:
                    traffic_jam_chance = 0
            else:
                traffic_jam_chance = neighbour_node_data["TrafficJamChance"]
            edge_length += neighbour_node_data["TrafficJamDelay"] * traffic_jam_chance

            if current_node.get_path_length() + edge_length < neighbour_node.get_path_length():
                neighbour_node.set_previous(current_node)
                if light_status == 1:   # If the light is green, the light status will be changed
                    neighbour_node.set_light_status_counter(
                        current_node.get_light_status_counter() + 1
                    )    
                neighbour_node.set_path_length(current_node.get_path_length() + edge_length)

        if is_starter_node:
            is_starter_node = False

        # Rearrange heap in order to get the node with the shortest path to the first place
        heapq.heapify(unvisited_nodes)


def find_shortest_path(starter_node, target_node, shortest_path):
    '''Shortest path from target to start'''
    shortest_path.append(target_node.get_name())

    # Making sure that it stops if there's no path between target and start
    if target_node.get_previous() and starter_node.get_name() != target_node.get_name():
        find_shortest_path(starter_node, target_node.get_previous(), shortest_path)


if __name__ == "__main__":
    with open(r"taskThree.json") as json_data:
        map = json.load(json_data)

    starter_node_name = sys.argv[1]
    target_node_name = "E4"
    all_nodes = {}

    starter_current_data = json.loads(sys.argv[2])

    # Check if status of lights has changed
    first_neighbour_node_name = next(iter(starter_current_data.keys()))
    light_status_is_normal = True
    if map[starter_node_name][first_neighbour_node_name]["TrafficLight"] != starter_current_data[first_neighbour_node_name]["RedLight"]:
        light_status_is_normal = False

    dijkstra(starter_node_name, map, all_nodes, light_status_is_normal, starter_current_data)

    shortest_path = []
    find_shortest_path(all_nodes[starter_node_name], all_nodes[target_node_name], shortest_path)
    shortest_path.reverse()
    try:
        sys.stdout.write(shortest_path[1])
    except:
        print("You are already at your target destination")


        