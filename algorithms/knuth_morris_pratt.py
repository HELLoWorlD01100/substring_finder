from algorithms.interface_algorithm import i_algorithm
from algorithms.algorithm_result import AlgorithmResult


class KnuthMorrisPrattAlgorithm(i_algorithm):
    def __init__(self, source: str, target: str):
        self._string = source
        self._pattern = target
        self._found_substrings_indexes = []
        self._current_indexes = ()
        self._str_index = 0
        self._pattern_index = 0
        self._pi = self.__get_prefix_func__(self._pattern)

    @staticmethod
    def __get_prefix_func__(pattern):
        pi = [0]*len(pattern)
        j = 0
        t = 1
        while t < len(pattern):
            if pattern[j] == pattern[t]:
                pi[t] = j + 1
                j += 1
                t += 1
            elif j == 0:
                pi[t] = 0
                t += 1
            else:
                j = pi[j - 1]
        return pi

    def pass_one_step(self):
        if (self._str_index < len(self._string) and
                self._pattern_index < len(self._pattern)):
            self._current_indexes = (self._str_index,)
            if (self._string[self._str_index] ==
                    self._pattern[self._pattern_index]):
                if self._pattern_index == len(self._pattern) - 1:
                    entry = self._str_index - len(self._pattern) + 1
                    self._found_substrings_indexes.append(entry)
                    self._pattern_index = 0
                else:
                    self._pattern_index += 1
                self._str_index += 1
            elif self._pattern_index:
                self._pattern_index = self._pi[self._pattern_index - 1]
            else:
                self._str_index += 1
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, False)
        else:
            self._current_indexes = ()
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, True)
