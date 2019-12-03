from utils.problem import *
import math
import itertools
import random
import matplotlib.pyplot as plt


class ProblemTSP(Problem):
    def init_from_file(self, raw):
        raw = raw.read().strip().split()
        self.n = int(raw.pop(0))
        self.villes = []
        while len(raw) > 0:
            ville = Ville(int(raw.pop(0)), int(raw.pop(0)), int(raw.pop(0)))
            self.villes.append(ville)

    def __repr__(self):
        return "TSP %s => n = %d" % (self.name, self.n)

    def compute_all_solutions(self):
        id_sol = 0
        solutions = []
        for sol in list(itertools.permutations(self.villes)):
            single_sol = [id_sol, self.compute_val(
                list(sol))] + [x.id for x in sol]
            solutions.append(single_sol)
            id_sol += 1
        return solutions

    def compute_val(self, vec):
        ville0 = Ville(0, 0, 0)
        val = ville0.distance_from(vec[0]) + vec[-1].distance_from(ville0)
        for i in range(0, len(vec)-1):
            val += vec[i].distance_from(vec[i+1])
        return val

    def get_random_solutions(self, sample_size=1):
        solutions = []
        vec = []
        for _ in range(0, sample_size):
            while True:
                vec = random.sample(range(0, self.n), self.n)
                if vec not in solutions:
                    break
            solutions.append(vec)

        return [SolutionTSP(self, [self.villes[y] for y in x]) for x in solutions]

    def get_greedy_start_vec(self):
        ville0 = Ville(0, 0, 0)
        villes = self.villes.copy()
        solution = [villes.pop(ville0.get_id_of_closest(villes))]
        while len(villes) > 0:
            solution.append(villes.pop(solution[-1].get_id_of_closest(villes)))
        return solution


class SolutionTSP(Solution):
    def __init__(self, problem, vec):
        Solution.__init__(self, problem)
        self.vec = vec

    def __repr__(self):
        return str(self.vec)

    def get_val(self):
        if self.val is not None:
            return self.val
        self.val = self.problem.compute_val(self.vec)
        return self.val

    def get_voisins(self):
        voisins = []
        for i in range(0, len(self.vec)):
            copy = self.vec.copy()
            tmp = copy[i]
            copy[i] = copy[(i+1) % len(self.vec)]
            copy[(i+1) % len(self.vec)] = tmp
            voisins.append(SolutionTSP(self.problem, copy))
        return voisins

    def pyplot(self):
        x = [0]+[v.x for v in self.vec]+[0]
        y = [0]+[v.y for v in self.vec]+[0]

        plt.plot(x, y)
        plt.show()


class Ville:
    def __init__(self, id_ville, x, y):
        self.id = id_ville
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.id)

    def distance_from(self, ville):
        return math.sqrt(math.pow(self.x-ville.x, 2) + math.pow(self.y-ville.y, 2))

    def get_id_of_closest(self, villes):
        minimum = math.inf
        min_id = 0
        for i in range(0, len(villes)):
            d = self.distance_from(villes[i])
            if d < minimum:
                minimum = d
                min_id = i
        return min_id
