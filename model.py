class RoadMap:
    """
    Class for graph that defines connections between given countries
    """

    def __init__(self, countries, add_route):
        self.countries = countries
        self.truck_map = self.create_roadmap(countries, add_route)

    def create_roadmap(self, countries, add_route):
        """
        This method makes sure that route from start to end is the same as from end to start
        """
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
        """
        Returns all countries in this map(graph)
        """
        return self.countries

    def get_adjacent_countries(self, country):
        """
        Returns the neighbors of the given country
        """
        neighborhood = []
        for adjoining_country in self.countries:
            if self.truck_map[country].get(adjoining_country, False):
                neighborhood.append(adjoining_country)
        return neighborhood

    def get_distance(self, country1, country2):
        """
        Returns the distance between two countries. In this particular project distance is irrelevant - it is always
        1 - but:
        a) it also indicates number of borders to travers
        b) if conditions of project change - counting real distances is possible
        """
        return self.truck_map[country1][country2]
