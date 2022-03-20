from algorithms.brut_force import BrutForceAlgorithm
from algorithms.knuth_morris_pratt import KnuthMorrisPrattAlgorithm
from algorithms.boyer_moore import BoyerMooreAlgorithm
from algorithms.rabin_karp import RabinKarpAlgorithm
from algorithms.interface_algorithm import i_algorithm


class Model:
    def __init__(self):
        self.current_algorithm = ''
        self.string = ''
        self.pattern = ''

    def set_algorithm(self, algorithm_name):
        if algorithm_name == 'Brut Force':
            self.current_algorithm = BrutForceAlgorithm(self.string, self.pattern)
        elif algorithm_name == 'Rabin-Karp':
            self.current_algorithm = RabinKarpAlgorithm(self.string, self.pattern)
        elif algorithm_name == 'Boyer-Moore':
            self.current_algorithm = BoyerMooreAlgorithm(self.string, self.pattern)
        elif algorithm_name == 'Knuth-Morris-Pratt':
            self.current_algorithm = KnuthMorrisPrattAlgorithm(self.string, self.pattern)
        else:
            raise NameError("Алгоритма с таким именем нету")
