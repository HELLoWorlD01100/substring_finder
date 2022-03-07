from algorithms.interface_algorithm import i_algorithm


class BoyerMooreAlgorithm(i_algorithm):
    def __init__(self, model):
        self._model = model
        self._string = self._model.string
        self._pattern = self._model.pattern
        self._offset_other_letters = len(self._pattern)
        self._offset_table = self.__get_offset_table__(self._pattern)
        self._curr_ind_str = len(self._pattern) - 1
        self._index = 0
        self._model.string_is_over = False

    def __get_offset_table__(self, pattern):
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

    def one_step_algorithm(self):
        if self._curr_ind_str < len(self._string):
            self._model.current_indexes = (self._curr_ind_str,)
            if self._index < len(self._pattern):
                current_index = self._curr_ind_str - self._index
                self._model.current_indexes = (current_index,)
                if (self._pattern[len(self._pattern) - 1 - self._index] !=
                        self._string[self._curr_ind_str - self._index]):
                    if (self._string[self._curr_ind_str - self._index]
                            in self._offset_table):
                        symbol = self._string[self._curr_ind_str - self._index]
                        transfer = self._offset_table[symbol]
                        self._curr_ind_str += transfer
                    else:
                        self._curr_ind_str += self._offset_other_letters
                    self._index = 0
                    return
                self._index += 1
            else:
                self._index = 0
                entry = self._curr_ind_str - len(self._pattern) + 1
                self._model.found_substrings_indexes.append(entry)
                self._curr_ind_str += 1
        else:
            self._model.string_is_over = True
            self._model.current_indexes = ()
