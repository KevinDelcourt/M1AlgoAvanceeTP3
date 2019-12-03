from utils.stats import *
from utils.algos import *
from tsp import *
from ubqp import *
from ubqpc import *
from tsp_plus import *
import math
# tsp5 -> plus de diff à partir de 5 déplacements
# tsp101 -> à partir de 60
# graphe12345 / bis -> 10 deplacements (en UBPQ avec ou sans contrainte)


def test_etude_stats_depl():
    #t = ProblemTSP("tsp5")
    t = ProblemUBQPC("graphe12345")
    #t = ProblemTSP("tsp101")
    #t = ProblemTSPPLUS("tsp101")
    etude_max_depl(t, range(0, 200, 20), 5)

# graphe12345 à partir de 3 c bon pour le tabou


def test_etude_stats_depl_tabou():
    #t = ProblemTSPPLUS("tsp5")
    #t = ProblemUBQPC("graphe12345")
    t = ProblemTSPPLUS("tsp101")
    etude_max_depl_tabou(t, range(0, 50, 25), range(0, 30, 10), 2)


def run():
    t = ProblemTSPPLUS("tsp101")
    #t = ProblemUBQPC("graphe12345")
    #mybad = SolutionTSPPLUS(t, [t.villes[x-1] for x in [1, 5, 4, 2, 3]])
    steepest_hill_climbing_redemarrage(
        t, steepest_hill_climbing, (math.inf), nb_essais=10)
    #steepest_hill_climbing(t, t.get_random_solutions()[0])
    #steepest_hill_climbing_tabou(   t, t.get_random_solutions()[0], (200, 5))


def main():
    run()


if __name__ == '__main__':
    main()
