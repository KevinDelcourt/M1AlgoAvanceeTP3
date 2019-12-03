from os import path


class Problem:
    def __init__(self, file_name):
        if not path.exists("./problems/"+file_name+".txt"):
            raise Exception("Mauvais chemin de fichier")

        self.name = file_name

        with open("./problems/"+file_name+".txt",
                  "r") as data_file:
            self.init_from_file(data_file)

    def init_from_file(self, raw):
        raise Exception("No")

    def get_random_solutions(self, sample_size=1):
        raise Exception("No")

    def meilleur_voisin_of_sol(self, sol):
        voisins = sol.get_voisins()
        return self.meilleur_of_sols(voisins)

    def meilleur_of_sols(self, solutions):
        best = None
        while len(solutions) > 0:
            sol = solutions.pop(0)
            if best is None:
                if sol.acceptable():
                    best = sol
            else:
                if sol.acceptable() and sol.meilleur_que(best):
                    best = sol
        return best


class Solution:
    def __init__(self, problem):
        self.problem = problem
        self.val = None

    def get_voisins(self):
        raise Exception("No")

    def get_val(self):
        raise Exception("No")

    def meilleur_que(self, another_sol):
        return self.get_val() < another_sol.get_val()

    def acceptable(self):
        return True

    def tostr(self):
        return str(self.get_val()) + " : " + self.__repr__()
