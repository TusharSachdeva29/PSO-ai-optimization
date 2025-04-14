def plot_grid(env, path=None):
    grid = env.grid.copy()
    plt.figure(figsize=(6, 6))
    for i in range(env.rows):
        for j in range(env.cols):
            if (i, j) in env.obstacles:
                color = 'black'
            elif (i, j) == env.start:
                color = 'green'
            elif (i, j) == env.goal:
                color = 'red'
            elif path and (i, j) in path:
                color = 'blue'
            else:
                color = 'white'
            plt.gca().add_patch(
                plt.Rectangle((j, env.rows - 1 - i), 1, 1, facecolor=color, edgecolor='gray')
            )
    plt.xlim(0, env.cols)
    plt.ylim(0, env.rows)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.show()
