import sys
from database.data_manager import get_all_shortcuts_of_countries, get_all_roads, get_all_countries, get_one_country
from validator import is_list_valid, is_shortcut_valid
from model import RoadMap


def get_list_from_db(func):
    try:
        data = func()
    except Exception as e:
        return []
    if is_list_valid(data):
        return data
    else:
        return []


def create_roadmap():
    # if destination exists in our database, code below creates data for road map - list of roads (connections)
    all_countries_shortcuts = get_list_from_db(get_all_shortcuts_of_countries)
    all_routes = get_list_from_db(get_all_roads)

    if all_countries_shortcuts and all_routes:
        add_route = {}
        for country in all_countries_shortcuts:
            add_route[country] = {}

        for route in all_routes:
            add_route[route.get("start")][route.get("end")] = route.get("distance")

        # here is created roadmap - for america in this case
        return RoadMap(all_countries_shortcuts, add_route)
    else:
        raise ValueError


def get_and_validate_country_shortcut_from_user(shortcut):
    if shortcut and is_shortcut_valid(shortcut):
        return shortcut.upper()
    else:
        return ''


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


def find_road_between(end_country, start_country):
    """
    Function finds shortest path from start to end
    :param end_country: string (shortcut)
    :param start_country: string (shortcut)
    :return: list of shortcuts of countries
    """
    roadmap = create_roadmap()
    all_countries = roadmap.countries
    start = get_and_validate_country_shortcut_from_user(start_country)
    destination = get_and_validate_country_shortcut_from_user(end_country)

    if start in all_countries and destination in all_countries:
        previous_countries = get_path_and_distance(roadmap, start)

        path = []
        via = destination
        while via != start:
            path.append(via)
            via = previous_countries[via]

        path.append(start)
        path.reverse()

        return path
    else:
        return ["There isn't {} or {} on our roadmap, sorry".format(start_country, end_country)]


def get_countries_between(end_country, start_country):
    """
    Function transforms list of shortcuts that make a path into list of countries
    :return: dictionary
    """
    countries = {}
    shortcuts = find_road_between(end_country, start_country)
    for short in shortcuts:
        country = get_one_country(short).get('country')
        countries.setdefault('countries', []).append(country)

    return countries


def get_countries():
    db = get_all_countries()
    return db
