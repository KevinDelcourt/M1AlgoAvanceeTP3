from utils.algos import steepest_hill_climbing, steepest_hill_climbing_tabou
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from utils.log import Log


def etude_max_depl(problem, range_dep, nb_essais):
    log = Log()
    solutions = problem.get_random_solutions(nb_essais)
    results = []
    for i in range_dep:
        inter = []
        for sol in solutions:
            inter.append(steepest_hill_climbing(
                problem, sol, (i), log=log)[2].get_val())
        results.append(sum(inter)/len(inter))

    plt.plot(range_dep, results)
    plt.show()


def etude_max_depl_tabou(problem, range_dep, range_tabou, nb_essais):
    log = Log()
    solutions = problem.get_random_solutions(nb_essais)
    results = []
    for i in range_dep:
        line = []
        for j in range_tabou:
            inter = []
            for sol in solutions:
                inter.append(steepest_hill_climbing_tabou(
                    problem, sol, (i, j), log=log)[2].get_val())
            line.append(sum(inter)/len(inter))
        results.append(line)

    fig = plt.figure()
    axes = fig.gca(projection='3d')

    z_ax = np.transpose(np.asarray(results))
    x_ax, y_ax = np.meshgrid(range_dep, range_tabou)
    axes.plot_surface(x_ax, y_ax, z_ax,
                      linewidth=0, antialiased=False)

    axes.set_xlabel("max_depl")
    axes.set_ylabel("k")

    plt.show()
