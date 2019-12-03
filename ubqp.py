from utils.problem import *
import random
import itertools
import math


class ProblemUBQP(Problem):

    def init_from_file(self, raw):
        raw = raw.read().strip().split(' ')
        self.n = int(raw.pop(0))
        self.p = int(raw.pop(0))
        self.mat = []
        for i in range(0, self.n):
            line = []
            for j in range(0, self.n):
                line.append(int(raw.pop(0)))
            self.mat.append(line)

    def __repr__(self):
        return "UBPQ %s => n = %d => p = %d" % (self.name, self.n, self.p)

    def compute_val(self, vec):
        val = 0
        for i in range(0, len(vec)):
            for j in range(0, len(vec)):
                val += self.mat[i][j]*vec[i]*vec[j]
        return val

    def get_random_solutions(self, sample_size=1):
        solutions = []
        vec = []
        for _ in range(0, sample_size):
            while True:
                vec = []
                for _ in range(0, self.n):
                    vec.append(random.randint(0, 1))
                if vec not in solutions:
                    break
            solutions.append(vec)
        return [SolutionUBQP(self, x) for x in solutions]


class SolutionUBQP(Solution):
    def __init__(self, problem, vec):
        Solution.__init__(self, problem)
        self.vec = list(vec)

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
            copy[i] = 1 - self.vec[i]
            voisins.append(SolutionUBQP(self.problem, copy))
        return voisins
