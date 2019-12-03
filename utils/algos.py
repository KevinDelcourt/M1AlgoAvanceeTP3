from utils.tabou import Tabou
from utils.log import Log
import math


def steepest_hill_climbing(problem, depart, args=(math.inf), log=None):
    (max_depl) = args

    if log is None:
        log = Log()
    log.write("START Steepest Hill Climbing", 2)
    log.write("MAX_DEPL = %s" % str(max_depl), 3)
    log.write(problem, 3)

    s = depart
    nb_depl = 0
    optimum_found = False
    while nb_depl < max_depl and not optimum_found:
        meilleur_voisin = problem.meilleur_voisin_of_sol(s)
        if meilleur_voisin is not None and meilleur_voisin.meilleur_que(s):
            log.write("step %d :\t %s" %
                      (nb_depl, s.tostr()), 5)
            nb_depl += 1
            s = meilleur_voisin
        else:
            optimum_found = True
    log.write("END Steepest Hill Climbing", 2)
    log.write("Depart : %s" % depart.tostr(), 3)
    log.write("Optimum local : %s" % s.tostr(), 3)
    log.write("Trouvé en %d déplacements" % nb_depl, 3)
    return (depart, nb_depl, s)


def steepest_hill_climbing_redemarrage(problem, methode, args, nb_essais=1, log=None):
    if log is None:
        log = Log()

    log.write("START Redémarrage", 0)
    log.write(problem, 1)
    log.write("%s essais" % str(nb_essais), 1)
    log.write("Methode : %s\n" % str(methode), 1)

    possible_starts = problem.get_random_solutions(nb_essais)
    best = []
    for solution in possible_starts:
        tmp = methode(problem, solution, args, log)
        if best == [] or tmp[2].meilleur_que(best[2]):
            best = tmp
            log.write("Nouvel optimum local : %s" %
                      best[2].tostr(), 1)

    log.write("END Redémarrage", 0)
    log.write("Depart : %s" % best[0].tostr(), 0)
    log.write("Optimum local : %s" % best[2].tostr(), 0)
    log.write("Trouvé en %d déplacements" % best[1], 0)

    return best


def steepest_hill_climbing_tabou(problem, depart, args=(math.inf, math.inf), log=None):
    (max_depl, k) = args

    if log is None:
        log = Log()
    log.write("START Tabou Hill Climbing", 2)
    log.write("MAX_DEPL = %s" % str(max_depl), 3)
    log.write("K = %s" % str(k), 3)
    log.write(problem, 3)

    best = depart
    s = depart
    tmp = None
    tabou = Tabou(k)
    nb_depl = 0
    optimum_found = False
    while not optimum_found and nb_depl < max_depl:
        log.write("step %d :\t %s" %
                  (nb_depl, s.tostr()), 5)
        voisins_non_tabous = [
            x for x in s.get_voisins() if x.acceptable() and x.vec not in [y.vec for y in tabou.list]]
        log.write("%d voisins non tabous (taille %d)" %
                  (len(voisins_non_tabous), len(tabou.list)), 6)
        if len(voisins_non_tabous) > 0:
            tmp = problem.meilleur_of_sols(voisins_non_tabous)
        else:
            optimum_found = True

        tabou.push_obj(s)

        if tmp.meilleur_que(best):
            best = tmp
            log.write("Nouvel optimum local : %s" %
                      best.tostr(), 4)
        s = tmp
        nb_depl += 1

    log.write("END Tabou Hill Climbing", 2)
    log.write("Tabou : %s" % str(tabou), 3)
    log.write("Depart : %s" % depart.tostr(), 3)
    log.write("Optimum local : %s" % best.tostr(), 3)
    log.write("%d déplacements effectués" % nb_depl, 3)

    return (depart, nb_depl, best, tabou)
