# Take user input for distance matrix
n = int(input("Enter number of cities: "))
distance_matrix = []

for i in range(n):
    print("Enter distances from city", i, "to all cities (space-separated):")
    row = input().split()
    row = [int(x) for x in row]
    distance_matrix.append(row)

# Generate all possible paths using recursion
def generate_routes(cities, position, all_routes):
    if position == len(cities):
        all_routes.append(cities[:])  # store a copy of the current route
        return

    for i in range(position, len(cities)):
        cities[position], cities[i] = cities[i], cities[position]
        generate_routes(cities, position + 1, all_routes)
        cities[position], cities[i] = cities[i], cities[position]  # backtrack

# Calculate total cost of a route
def calculate_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    cost += distance_matrix[route[-1]][route[0]]  # return to starting city
    return cost

# Main TSP logic
def solve_tsp():
    cities = list(range(n))  # dynamic city list from input size
    all_routes = []

    generate_routes(cities, 0, all_routes)

    best_path = all_routes[0]
    lowest_cost = calculate_cost(best_path)

    for path in all_routes[1:]:
        cost = calculate_cost(path)
        if cost < lowest_cost:
            lowest_cost = cost
            best_path = path

    print("\nBest path:", best_path)
    print("Minimum cost:", lowest_cost)

# Run the function
solve_tsp()
