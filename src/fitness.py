def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def fitness_function(path, grid_env, w1=0.4, w2=0.3, w3=0.2, w4=0.1):
    distance = 0
    energy = 0
    collisions = 0

    for i in range(len(path) - 1):
        distance += euclidean_distance(path[i], path[i+1])
        if not grid_env.is_valid(path[i]):
            collisions += 1
        energy += 1  # placeholder

    time = len(path)
    return w1 * distance + w2 * time + w3 * energy + w4 * collisions

