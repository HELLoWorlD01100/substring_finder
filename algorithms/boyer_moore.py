from algorithms.interface_algorithm import i_algorithm
from algorithms.algorithm_result import AlgorithmResult


class BoyerMooreAlgorithm(i_algorithm):
    def __init__(self, source: str, target: str):
        self._current_indexes = ()
        self._found_substrings_indexes = []
        self._string = source
        self._pattern = target
        self._offset_other_letters = len(self._pattern)
        self._offset_table = self.__get_offset_table__(self._pattern)
        self._current_index_string = len(self._pattern) - 1
        self._index = 0

    @staticmethod
    def __get_offset_table__(pattern):
        index = len(pattern) - 2
        result = {}
        while index >= 0:
            if pattern[index] not in result:
                result[pattern[index]] = len(pattern) - index - 1
            index = index - 1
        else:
            if pattern[len(pattern) - 1] not in result:
                result[pattern[len(pattern) - 1]] = len(pattern)
        return result

    def pass_one_step(self):
        if self._current_index_string < len(self._string):
            self._current_indexes = (self._current_index_string,)
            if self._index < len(self._pattern):
                current_index = self._current_index_string - self._index
                self._current_indexes = (current_index,)
                if (self._pattern[len(self._pattern) - 1 - self._index] !=
                        self._string[self._current_index_string - self._index]):
                    if (self._string[self._current_index_string - self._index]
                            in self._offset_table):
                        symbol = self._string[self._current_index_string - self._index]
                        transfer = self._offset_table[symbol]
                        self._current_index_string += transfer
                    else:
                        self._current_index_string += self._offset_other_letters
                    self._index = 0
                else:
                    self._index += 1
            else:
                self._index = 0
                entry = self._current_index_string - len(self._pattern) + 1
                self._found_substrings_indexes.append(entry)
                self._current_index_string += 1

            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, False)
        else:
            self._current_indexes = ()
            return AlgorithmResult(self._found_substrings_indexes, self._current_indexes, True)
