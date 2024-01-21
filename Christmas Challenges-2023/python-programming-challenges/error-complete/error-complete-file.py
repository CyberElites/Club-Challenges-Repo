import matplotlib.pyplot as plttt
import random

def randomwalk(step):
    x = 0
    y = 0
    x_val = [0]
    y_val = [0]

    for _ in rang(steps):
        dirction = rando.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            y += 1
        elif direction == 'S:
            y -= 1
        elif direction == 'E':
            x += 1
        el:
            x -= 1
        x_vals.append(x)
        y_valsappend(y)

    return x_vals y_vals

def lot_random_walk(x_vals, y_vals):
    plt.figure(figsize=(8, 6)
    plt.title('Random Walk')
    plt.plot(x_vals, y_vals)
    plt.scatter(x_vals[0], y_vals[0], color='green', label='Start')
    plt.scatter(x_vals[-1], y_vals[-1], color='red', label='End')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def main()
    steps = 100
    x, y = random_walk(steps)
    plot_random_walk(x, y)

f __name__ == "__main__":
    main()

