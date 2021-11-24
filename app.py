import sys
from database.data_manager import get_all_countries, get_all_borders


class RoadMap:
    def __init__(self, countries, add_route):
        self.countries = countries
        self.truck_map = self.create_roadmap(countries, add_route)

    def create_roadmap(self, countries, add_route):
        roadmap = {}
        for country in countries:
            roadmap[country] = {}

        roadmap.update(add_route)

        for country, area in roadmap.items():
            for adjacent_country, distance in area.items():
                if not roadmap[adjacent_country].get(country, False):
                    roadmap[adjacent_country][country] = distance
        return roadmap

    def get_countries(self):
        return self.countries

    def get_adjacent_countries(self, country):
        neighborhood = []
        for adjoining_country in self.countries:
            if self.truck_map[country].get(adjoining_country, False):
                neighborhood.append(adjoining_country)
        return neighborhood

    def get_distance(self, country1, country2):
        return self.truck_map[country1][country2]


def get_path_and_distance(roadmap, start_country):
    unvisited_countries = list(roadmap.get_countries())
    shortest_path = {}
    previous_countries = {}
    max_value = sys.maxsize
    for country in unvisited_countries:
        shortest_path[country] = max_value
    shortest_path[start_country] = 0

    while unvisited_countries:
        current_country = None
        for country in unvisited_countries:
            if current_country is None:
                current_country = country
            elif shortest_path[country] < shortest_path[current_country]:
                current_country = country

        neighbors = roadmap.get_adjacent_countries(current_country)
        for neighbor in neighbors:
            temp_distance = shortest_path[current_country] + roadmap.get_distance(current_country, neighbor)
            if temp_distance < shortest_path[neighbor]:
                shortest_path[neighbor] = temp_distance
                previous_countries[neighbor] = current_country

        unvisited_countries.remove(current_country)

    return previous_countries, shortest_path


def get_countries_list():
    countries = []
    db_result = get_all_countries()
    for record in db_result:
        countries.append(record.get("shortcut"))
    return countries


def get_routes():
    routes = get_all_borders()
    return routes


all_countries = get_countries_list()
add_route = {}
for country in all_countries:
    add_route[country] = {}

all_routes = get_routes()
for route in all_routes:
    add_route[route.get("start")][route.get("end")] = route.get("distance")

roadmap_america = RoadMap(all_countries, add_route)

previous_countries, shortest_path = get_path_and_distance(roadmap_america, "USA")


# def print_result(previous, path2, start_node, target_node):
#     path = []
#     node = target_node
#
#     while node != start_node:
#         path.append(node)
#         node = previous[node]
#
#     # Add the start node manually
#     path.append(start_node)
#
#     print("We found the following best path with a value of {}.".format(path2[target_node]))
#     print(" -> ".join(reversed(path)))
#
#
# print_result(previous_countries, shortest_path, "USA", "PAN")

def find_countries_and_path(countries, start_country, end_country):
    path = []
    country = end_country
    while country != start_country:
        path.append(country)
        country = countries[country]

    path.append(start_country)
    reversed_path = ",".join(reversed(path))

    return reversed_path

# print(find_countries_and_path(previous_countries, "USA", "PAN"))

path_to_target = find_countries_and_path(previous_countries, "USA", "PAN")