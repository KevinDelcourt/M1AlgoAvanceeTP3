from ubqp import *


class ProblemUBQPC(ProblemUBQP):
    def init_solutions_from_file(self, raw):
        reader = csv.reader(raw)
        self.solutions = []
        for row in reader:
            self.solutions.append(SolutionUBQPC(list(map(int, row)), self.p))
        self.solutions_acceptables = [
            x for x in self.solutions if x.acceptable()]


class SolutionUBQPC(SolutionUBQP):
    def __init__(self, args, p):
        SolutionUBQP.__init__(self, args)
        self.problem_p = p

    def acceptable(self):
        return self.p >= self.problem_p
