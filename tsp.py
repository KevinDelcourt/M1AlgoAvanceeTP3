from utils.problem import *
import itertools
import math


class ProblemTSP(Problem):
    def init_from_file(self, raw):
        raw = raw.read().strip().split()
        self.n = int(raw.pop(0))
        self.villes = []
        while len(raw) > 0:
            ville = Ville(int(raw.pop(0)), int(raw.pop(0)), int(raw.pop(0)))
            self.villes.append(ville)

    def __repr__(self):
        return "\n============\nTSP %s\nn = %d\n============\n" % (self.name, self.n)

    def compute_all_solutions(self):
        id_sol = 0
        solutions = []
        possible_permutations = list(itertools.permutations(self.villes))
        for sol in possible_permutations:
            single_sol = [id_sol, self.compute_valeur(
                list(sol))] + [x.id for x in sol]
            solutions.append(single_sol)
            id_sol += 1
            if id_sol % math.trunc(len(possible_permutations)/100) == 0:
                print(id_sol)
        return solutions

    def compute_valeur(self, sol):
        ville0 = Ville(0, 0, 0)
        val = ville0.distance_from(sol[0]) + sol[-1].distance_from(ville0)
        for i in range(0, len(sol)-1):
            val += sol[i].distance_from(sol[i+1])
        return val

    def init_solutions_from_file(self, raw):
        reader = csv.reader(raw)
        self.solutions = []
        for row in reader:
            self.solutions.append(SolutionTSP(list(row), self))
        print(self.solutions[0].get_voisins_ids())
        self.solutions_acceptables = self.solutions


class SolutionTSP(Solution):
    def __init__(self, args, problem):
        self.id = int(args.pop(0))
        self.val = float(args.pop(0))
        self.vec = list(map(int, args))
        self.problem = problem

    def __repr__(self):
        return "Sol(%d,%d)" % (self.id, self.val)

    def get_id_of_vec(self, vec):
        return next(x.id for x in self.problem.solutions if x.vec == vec)

    def get_voisins_ids(self):
        ids = []
        for i in range(0, len(self.vec)):
            copy = self.vec.copy()
            tmp = copy[i]
            copy[i] = copy[(i+1) % len(self.vec)]
            copy[(i+1) % len(self.vec)] = tmp
            ids.append(self.get_id_of_vec(copy))
        return ids

    def acceptable(self):
        return True


class Ville:
    def __init__(self, id_ville, x, y):
        self.id = id_ville
        self.x = x
        self.y = y

    def __repr__(self):
        return "Ville(%d,%d)" % (self.x, self.y)

    def distance_from(self, ville):
        return math.sqrt(math.pow(self.x-ville.x, 2) + math.pow(self.y-ville.y, 2))
