from algorithms.interface_algorithm import i_algorithm
from algorithms.algorithm_result import AlgorithmResult


class BrutForceAlgorithm(i_algorithm):
    def __init__(self, source: str, target: str):
        self._current_indexes = ()
        self._found_substrings_indexes = []
        self._string = source
        self._pattern = target
        self._str_index = 0
        self._pattern_index = 0

    def pass_one_step(self):
        if self._str_index < len(self._string) - len(self._pattern) + 1:
            if self._pattern_index < len(self._pattern):
                self._current_indexes = (self._str_index +
                                         self._pattern_index,)
                if (self._pattern[self._pattern_index] !=
                        self._string[self._str_index + self._pattern_index]):
                    self._pattern_index = 0
                    self._str_index += 1
                else:
                    self._pattern_index += 1
            else:
                self._found_substrings_indexes.append(self._str_index)
                self._pattern_index = 0
                self._str_index += 1
        else:
            self._current_indexes = ()
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, True)

        return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, False)
