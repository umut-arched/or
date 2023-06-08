from util import read_instance_from_file, euclidean_distance, plot_coordinates
def cheapest_insertion(coords):
    airports = list(range(0, len(coords), 1)) # (1...10)
    v = airports[0]
    hamilton = [v] #(1, 1)

    while len(hamilton) < len(airports):
        unvisitedAirports = [airport for airport in airports if airport not in hamilton] # (2..10)
        closestAirport = None
        min_distance = float('inf')
        for airport in unvisitedAirports:
            distance = euclidean_distance(coords[v], coords[airport])
            if distance < min_distance:
                min_distance = distance
                closestAirport = airport
        hamilton.append(closestAirport)
    hamilton.append(0)
    totalDistance = sum(euclidean_distance(coords[hamilton[i]], coords[hamilton[i+1]]) for i in range(len(hamilton)-1))
    return hamilton, float(totalDistance)


if __name__ == "__main__":
    coords = read_instance_from_file("./data/eins.txt")
    route, totalDistance = cheapest_insertion(coords)
    plot_coordinates(coords, route)
    print(route)
    print(totalDistance)