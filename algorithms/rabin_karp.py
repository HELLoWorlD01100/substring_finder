from algorithms.interface_algorithm import i_algorithm


class RabinKarpAlgorithm(i_algorithm):
    def __init__(self, model):
        self._model = model
        self._string = self._model.string
        self._pattern = self._model.pattern
        self._prime = 255
        substring = self._string[0:len(self._pattern)]
        self._substr_hash = self.__get_hash_code__(substring)
        self._pattern_hash = self.__get_hash_code__(self._pattern)
        self._str_index = 0
        self._pattern_index = 0
        self._model.string_is_over = False

    def __get_hash_code__(self, string):
        hash = 0
        power = 0
        for letter in string:
            hash += ord(letter) * (self._prime ** power)
            power += 1
        return hash

    def one_step_algorithm(self):
        if self._str_index < len(self._string) - len(self._pattern) + 1:
            self._model.current_indexes = tuple(
                j for j in range(self._str_index, self._str_index +
                                 len(self._pattern)))
            if self._pattern_hash == self._substr_hash:
                if self._pattern_index < len(self._pattern):
                    self._model.current_indexes = (self._str_index +
                                                   self._pattern_index,)
                    if (self._pattern[self._pattern_index] !=
                            self._string[self._str_index +
                                         self._pattern_index]):
                        self._pattern_index = 0
                        self.recalculate_substring_hash()
                        self._str_index += 1
                        return
                    else:
                        self._pattern_index += 1
                else:
                    self._model.found_substrings_indexes.append(
                        self._str_index)
                    self._pattern_index = 0
                    self.recalculate_substring_hash()
                    self._str_index += 1
            else:
                self._pattern_index = 0
                self.recalculate_substring_hash()
                self._str_index += 1
        else:
            self._model.string_is_over = True
            self._model.current_indexes = ()

    def recalculate_substring_hash(self):
        if self._str_index != len(self._string) - len(self._pattern):
            self._substr_hash -= ord(self._string[self._str_index])
            self._substr_hash = int(self._substr_hash / self._prime)
            symbol = self._string[self._str_index + len(self._pattern)]
            self._substr_hash += (ord(symbol) *
                                  (self._prime ** (len(self._pattern) - 1)))
