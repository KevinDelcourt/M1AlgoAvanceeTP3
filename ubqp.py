from os import path
import itertools
import csv
import random

from utils.problem import *


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

    def init_solutions_from_file(self, raw):
        reader = csv.reader(raw)
        self.solutions = []
        for row in reader:
            self.solutions.append(SolutionUBQP(list(map(int, row))))
        self.solutions_acceptables = self.solutions

    def __repr__(self):
        return "\n============\n" + "UBPQ\n" + \
            ("n = %d\n" % self.n) + ("p = %d\n============\n" % self.p)

    def compute_all_solutions(self):
        id_sol = 0
        solutions = []
        for sol in list(itertools.product([0, 1], repeat=self.n)):
            single_sol = [id_sol, self.compute_valeur(list(sol))] + list(sol)
            solutions.append(single_sol)
            id_sol += 1
        return solutions

    def compute_valeur(self, solution):
        val = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                val += self.mat[i][j]*solution[i]*solution[j]
        return val


class SolutionUBQP(Solution):
    def __init__(self, args):
        self.id = args.pop(0)
        self.val = args.pop(0)
        self.vec = args
        self.p = sum(self.vec)

    def __repr__(self):
        return "Sol(%d,%d,%d)" % (self.id, self.val, self.p)

    def get_id_of_vec(self, vec):
        value = 0
        for i in range(0, len(vec)):
            value += pow(2, len(vec)-1-i)*vec[i]
        return value

    def get_voisins_ids(self):
        ids = []
        for i in range(0, len(self.vec)):
            copy = self.vec.copy()
            copy[i] = 1 - self.vec[i]
            ids.append(self.get_id_of_vec(copy))
        return ids

    def acceptable(self):
        return True
