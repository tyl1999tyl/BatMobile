# Recursive function to print the path of given vertex `u` from source vertex `v`
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
 
 
# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                route_l =  [x+1 for x in route]
                
                print(f'The shortest path from {v+1} —> {u+1} is', route_l)
 
 
# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix):
 
    # base case
    if not adjMatrix:
        return
 
    # total number of vertices in the `adjMatrix`
    n = len(adjMatrix)
 
    # cost and path matrix stores shortest path
    # (shortest cost/shortest route) information
 
    # initially, cost would be the same as the weight of an edge
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]
 
    # initialize cost and path
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1
 
    # run Floyd–Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # If vertex `k` is on the shortest path from `v` to `u`,
                # then update the value of cost[v][u] and path[v][u]
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
 
            # if diagonal elements become negative, the
            # graph contains a negative-weight cycle
            if cost[v][v] < 0:
                print('Negative-weight cycle found')
                return
 
    # Print the shortest path between all pairs of vertices
    printSolution(path, n)
    
if __name__ == '__main__':

    # define infinity
    I = float('inf')

    # given adjacency representation of the matrix
    adjMatrix = [
        [0, 5, I, I, I, I, I, I, I, I],
        [5, 0, 5, I, I, I, I, I, 7, I],
        [I, 5, 0, 5, I, I, I, I, I, I],
        [I, I, 5, 0, 3, 5, I, I, I, I],
        [I, I, I, 3, 0, I, I, I, I, I],
        [I, I, I, 5, I, 0, 6, I, I, I],
        [I, I, I, I, I, 6, 0, 3, I, I],
        [I, I, I, I, I, I, 3, 0, 1, I],
        [I, I, I, I, I, I, I, 1, 0, 1],
        [I, I, I, I, I, I, I, I, 1, 0],

    ]

    # Run Floyd–Warshall algorithm
    floydWarshall(adjMatrix)