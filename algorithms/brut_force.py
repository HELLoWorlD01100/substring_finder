from algorithms.interface_algorithm import i_algorithm


class BrutForceAlgorithm(i_algorithm):
    def __init__(self, model):
        self._model = model
        self._string = self._model.string
        self._pattern = self._model.pattern
        self._str_index = 0
        self._pattern_index = 0
        self._model.string_is_over = False

    def one_step_algorithm(self):
        if self._str_index < len(self._string) - len(self._pattern) + 1:
            if self._pattern_index < len(self._pattern):
                self._model.current_indexes = (self._str_index +
                                               self._pattern_index,)
                if (self._pattern[self._pattern_index] !=
                        self._string[self._str_index + self._pattern_index]):
                    self._pattern_index = 0
                    self._str_index += 1
                    return
                else:
                    self._pattern_index += 1
            else:
                self._model.found_substrings_indexes.append(self._str_index)
                self._pattern_index = 0
                self._str_index += 1
        else:
            self._model.string_is_over = True
            self._model.current_indexes = ()
