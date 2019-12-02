from os import path
import itertools
import csv
import random


class Problem:

    def __init__(self, file_name):
        if not path.exists("./problems/"+file_name+".txt"):
            raise Exception("Mauvais chemin de fichier")

        self.name = file_name

        with open("./problems/"+file_name+".txt",
                  "r") as data_file:
            self.init_from_file(data_file)

        self.solutions = []
        if not path.exists("./solutions/"+file_name+".csv"):
            print("\033[1;33mCalcul de la base de solution\033[0m")
            with open("./solutions/"+file_name+".csv", 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(self.compute_all_solutions())

        with open("./solutions/"+file_name+".csv", 'r') as csv_file:
            self.init_solutions_from_file(csv_file)

    def init_from_file(self, raw):
        raise Exception("No")

    def init_solutions_from_file(self, raw):
        raise Exception("No")

    def __repr__(self):
        raise Exception("No")

    def compute_all_solutions(self):
        raise Exception("No")

    def meilleur_voisin(self, sol=None, ids=None):
        if ids is None:
            ids = sol.get_voisins_ids()
        best = self.solutions[ids[0]]
        for i in range(1, len(ids)):
            if self.solutions[ids[i]].meilleur_que(best) and self.solutions[ids[i]].acceptable() or not best.acceptable():
                best = self.solutions[ids[i]]

        if best.acceptable():
            return best

        return None


class Solution:
    def __init__(self, args):
        self.id = 0
        self.val = 0
        raise Exception("No")

    def __repr__(self):
        raise Exception("No")

    def get_voisins_ids(self):
        raise Exception("No")

    def meilleur_que(self, another_sol):
        return self.val < another_sol.val

    def acceptable(self):
        raise Exception("No")
