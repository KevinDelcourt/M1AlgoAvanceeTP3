from tsp import *

# Diff avec tsp --> voisin = toutes les permutations possibles ( pas juste les adjacents)


class ProblemTSPPLUS(ProblemTSP):
    def get_random_solutions(self, sample_size=1):
        solutions = []
        vec = []
        for _ in range(0, sample_size):
            while True:
                vec = random.sample(range(0, self.n), self.n)
                if vec not in solutions:
                    break
            solutions.append(vec)

        return [SolutionTSPPLUS(self, [self.villes[y] for y in x]) for x in solutions]


class SolutionTSPPLUS(SolutionTSP):
    def get_voisins(self):
        voisins = []
        for i in range(0, len(self.vec)):
            for j in range(i+1, len(self.vec)):
                copy = self.vec.copy()
                tmp = copy[i]
                copy[i] = copy[j]
                copy[j] = tmp
                voisins.append(SolutionTSPPLUS(self.problem, copy))
        return voisins
