from algorithms.interface_algorithm import i_algorithm
from algorithms.algorithm_result import AlgorithmResult


class RabinKarpAlgorithm(i_algorithm):
    def __init__(self, source: str, target: str):

        self._string = source
        self._pattern = target
        self._found_substrings_indexes = []
        self._current_indexes = ()
        self._prime = 255
        substring = self._string[0:len(self._pattern)]
        self._substr_hash = self.__get_hash_code__(substring)
        self._pattern_hash = self.__get_hash_code__(self._pattern)
        self._str_index = 0
        self._pattern_index = 0

    def __get_hash_code__(self, string):
        hash_value = 0
        power = 0
        for letter in string:
            hash_value += ord(letter) * (self._prime ** power)
            power += 1
        return hash_value

    def pass_one_step(self):
        if self._str_index < len(self._string) - len(self._pattern) + 1:
            self._current_indexes = tuple(
                j for j in range(self._str_index, self._str_index +
                                 len(self._pattern)))
            if self._pattern_hash == self._substr_hash:
                if self._pattern_index < len(self._pattern):
                    self._current_indexes = (self._str_index +
                                             self._pattern_index,)
                    if (self._pattern[self._pattern_index] !=
                            self._string[self._str_index +
                                         self._pattern_index]):
                        self._pattern_index = 0
                        self.__recalculate_substring_hash__()
                        self._str_index += 1

                    else:
                        self._pattern_index += 1
                else:
                    self._found_substrings_indexes.append(
                        self._str_index)
                    self._pattern_index = 0
                    self.__recalculate_substring_hash__()
                    self._str_index += 1
            else:
                self._pattern_index = 0
                self.__recalculate_substring_hash__()
                self._str_index += 1
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, False)
        else:
            self._current_indexes = ()
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, True)

    def __recalculate_substring_hash__(self):
        if self._str_index != len(self._string) - len(self._pattern):
            self._substr_hash -= ord(self._string[self._str_index])
            self._substr_hash = int(self._substr_hash / self._prime)
            symbol = self._string[self._str_index + len(self._pattern)]
            self._substr_hash += (ord(symbol) *
                                  (self._prime ** (len(self._pattern) - 1)))
