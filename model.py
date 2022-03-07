from algorithms.brut_force import BrutForceAlgorithm
from algorithms.knuth_morris_pratt import KnuthMorrisPrattAlgorithm
from algorithms.boyer_moore import BoyerMooreAlgorithm
from algorithms.rabin_karp import RabinKarpAlgorithm


class Model:
    def __init__(self):
        self.current_algorithm = ''
        self.string = ''
        self.pattern = ''
        self.current_indexes = ()
        self.found_substrings_indexes = []
        self.string_is_over = False

    def select_algorithm(self, algorithm_name):
        if algorithm_name == 'Brut Force':
            return BrutForceAlgorithm(self).one_step_algorithm
        if algorithm_name == 'Rabin-Karp':
            return RabinKarpAlgorithm(self).one_step_algorithm
        if algorithm_name == 'Boyer-Moore':
            return BoyerMooreAlgorithm(self).one_step_algorithm
        if algorithm_name == 'Knuth-Morris-Pratt':
            return KnuthMorrisPrattAlgorithm(self).one_step_algorithm
        raise NameError("Алгоритма с таким именем нету")
