from ubqp import *


class ProblemUBQPC(ProblemUBQP):
    def get_random_solutions(self, sample_size=1):
        solutions = []
        vec = []
        for _ in range(0, sample_size):
            while True:
                vec = []
                for _ in range(0, self.n):
                    vec.append(random.randint(0, 1))
                if vec not in solutions and sum(vec) >= self.p:
                    break
            solutions.append(vec)
        return [SolutionUBQPC(self, x) for x in solutions]


class SolutionUBQPC(SolutionUBQP):
    def acceptable(self):
        return sum(self.vec) >= self.problem.p
