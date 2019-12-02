from ubqp import *
from ubqpc import *
from tsp import *

from utils.tabou import Tabou
import math
import random


def print_intro_if_verbose(sol, verbose=False):
    if verbose:
        print("\n\033[1;35mSteepest Hill Climbing\033[0m")
        print("\033[0;35mDepart = " +
              sol.__repr__() + "\033[0m")


def print_s_if_verbose(sol, verbose=False):
    if verbose:
        print("\033[0;33m" +
              sol.__repr__() + "\033[0m")


def print_final_if_verbose(sol, verbose=False):
    if verbose:
        print("\033[1;36m" + sol.__repr__() + "\033[0m\n")


def steepest_hill_climbing(problem, depart, max_depl=math.inf, verbose=False):
    print_intro_if_verbose(depart, verbose)
    s = depart
    nb_depl = 0
    optimum_found = False
    while nb_depl < max_depl and not optimum_found:
        meilleur_voisin = problem.meilleur_voisin(s)
        nb_depl += 1
        if meilleur_voisin is not None and meilleur_voisin.meilleur_que(s):
            s = meilleur_voisin
            print_s_if_verbose(s, verbose)
        else:
            optimum_found = True
    print_final_if_verbose(s, verbose)
    return (s, nb_depl)


def steepest_hill_climbing_redemarrage(problem, max_depl=math.inf, max_essais=1000, verbose=0):
    nb_essais = max_essais
    if len(problem.solutions_acceptables) < nb_essais:
        nb_essais = len(problem.solutions_acceptables)

    possible_starts = random.sample(problem.solutions_acceptables, nb_essais)
    best = (possible_starts[0], 0)
    for solution in possible_starts:
        tmp = steepest_hill_climbing(problem, solution, max_depl, verbose > 2)
        if verbose > 1:
            print("\033[0;33m" + solution.__repr__() +
                  "\t => \t" + tmp[0].__repr__()+"\033[0m")
        if tmp[0].meilleur_que(best[0]):
            best = tmp

    if verbose > 0:
        print("\033[1;35mSteepest Hill Climbing avec rédémarrage\033[0m")
        print("\033[0;35m%d essais parmis %d\033[0m" %
              (nb_essais, len(problem.solutions)))
        print(problem)
        print("\033[1;36mRésultat : " + best[0].__repr__() +
              " en %d déplacements\033[0m\n" % best[1])
    return best


def steepest_hill_climbing_tabou(problem, depart, max_depl=math.inf, verbose=False, k=math.inf):
    best = depart
    s = depart
    tmp = None
    tabou = Tabou(k=k, verbose=verbose)
    nb_depl = 0
    optimum_found = False

    while not optimum_found and nb_depl < max_depl:
        voisins_non_tabous = [
            x for x in s.get_voisins_ids() if x not in tabou.list]
        if len(voisins_non_tabous) > 0:
            tmp = problem.meilleur_voisin(ids=voisins_non_tabous)
        else:
            optimum_found = True

        tabou.push_obj(s.id)

        if tmp is not None and tmp.meilleur_que(best):
            best = tmp
        if tmp is not None:
            s = tmp
        else:
            optimum_found = True

        nb_depl += 1

    return (best, nb_depl)


test2 = ProblemTSP("tsp101")
steepest_hill_climbing_redemarrage(
    test2, max_depl=math.inf, max_essais=25, verbose=2)

#test = ProblemUBQPC("partition6")
# print(steepest_hill_climbing_redemarrage(
#    test, max_depl=30, max_essais=10, verbose=1))

#sol = random.choice(test.solutions)

# print(steepest_hill_climbing_tabou(
#    test, sol, max_depl=200, verbose=False, k=math.inf))
