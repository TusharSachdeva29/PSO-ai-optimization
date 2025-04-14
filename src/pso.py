import random
from fitness import fitness_function

class Particle:
    def __init__(self, path):
        self.position = path
        self.velocity = []
        self.best_position = list(path)
        self.best_score = float('inf')

class PSO:
    def __init__(self, env, swarm_size=30, iterations=100):
        self.env = env
        self.swarm_size = swarm_size
        self.iterations = iterations
        self.swarm = []
        self.global_best = None
        self.global_best_score = float('inf')
        self.fitness_history = []  # Added to track fitness over iterations

    def generate_random_path(self):
        path = [self.env.start]
        while path[-1] != self.env.goal:
            x, y = path[-1]
            moves = [(0,1), (1,0), (0,-1), (-1,0)]
            random.shuffle(moves)
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if self.env.is_valid((nx, ny)) and (nx, ny) not in path:
                    path.append((nx, ny))
                    break
            else:
                break
        return path

    def optimize(self):
        self.swarm = [Particle(self.generate_random_path()) for _ in range(self.swarm_size)]
        self.fitness_history = []  # Initialize fitness history

        for _ in range(self.iterations):
            for particle in self.swarm:
                score = fitness_function(particle.position, self.env)

                if score < particle.best_score:
                    particle.best_score = score
                    particle.best_position = list(particle.position)

                if score < self.global_best_score:
                    self.global_best_score = score
                    self.global_best = list(particle.position)
            
            # Record the best score of this iteration
            self.fitness_history.append(self.global_best_score)

            for particle in self.swarm:
                particle.position = self.mutate_path(particle.best_position)

        return self.global_best

    def mutate_path(self, path):
        new_path = list(path)
        if len(new_path) > 2:
            i = random.randint(1, len(new_path)-2)
            new_path[i] = (new_path[i][0] + random.choice([-1,0,1]), new_path[i][1] + random.choice([-1,0,1]))
        return new_path
