import sys
from database.data_manager import get_all_shortcuts_of_countries, get_all_roads
from model import RoadMap


def get_path_and_distance(roadmap, start_country):
    """
    Function uses dijkstra's algorithm to calculate shortest paths from start
    and finds list of countries of which that paths are composed
    """

    # Gets all countries from roadmap
    unvisited_countries = list(roadmap.get_countries())

    # This dictionary will store distances(or in other words - borders) that must be travers
    # to visit every country
    distance = {}

    # This dictionary will store all countries for shortest path from start to end
    previous_countries = {}

    # The distance between countries at first is set as infinity (sort of) because we don't know real values.
    # It will be gradually updated
    max_value = sys.maxsize
    for country in unvisited_countries:
        distance[country] = max_value
    distance[start_country] = 0

    # This loop is executed until we visit all countries.
    while unvisited_countries:
        current_country = None

        # This loop iterates over countries anf finds shortest distance
        for country in unvisited_countries:
            if current_country is None:
                current_country = country
            elif distance[country] < distance[current_country]:
                current_country = country

        # This code checks for countries that are connected directly (borders with each other)
        neighbors = roadmap.get_adjacent_countries(current_country)
        for neighbor in neighbors:
            temp_distance = distance[current_country] + roadmap.get_distance(current_country, neighbor)
            if temp_distance < distance[neighbor]:
                distance[neighbor] = temp_distance
                previous_countries[neighbor] = current_country

        unvisited_countries.remove(current_country)

    return previous_countries


def find_countries_and_path(end_country, start_country):
    """
    Function create roadmap and finds shortest path between given countries
    """

    # get list of all countries for our roadmap
    all_countries = get_all_shortcuts_of_countries()

    # if destination exists in our database, code below creates data for road map - list of roads (connections)
    if end_country.upper() in all_countries:
        add_route = {}
        for country in all_countries:
            add_route[country] = {}

        all_routes = get_all_roads()
        for route in all_routes:
            add_route[route.get("start")][route.get("end")] = route.get("distance")

        # here is created roadmap - for america in this case
        roadmap_america = RoadMap(all_countries, add_route)

        previous_countries = get_path_and_distance(roadmap_america, start_country)

        # here the results of upper calculation are formatted
        path = []
        country = end_country.upper()
        while country != start_country:
            path.append(country)
            country = previous_countries[country]

        path.append(start_country)
        reversed_path = ",".join(reversed(path))

        return reversed_path, end_country.upper()
    else:
        return ["There isn't this country on our roadmap, sorry"], end_country

