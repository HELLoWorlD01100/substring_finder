from side_panel import SidePanel


class View:
    def __init__(self, root, model):
        self.__set_size__(root)
        self._root = root
        self._side_panel = SidePanel(root)
        self._model = model
        self._side_panel.text.insert(1.0, self._model.string)
        self._side_panel.pattern_entry.insert(1, self._model.pattern)
        self._side_panel.text.tag_config('goldbackground', background='gold')
        self._side_panel.text.tag_config('redforeground', foreground='red')
        self._side_panel.button_start['command'] = self.__start_button_act__
        self._side_panel.button_finish['state'] = 'disabled'
        self._side_panel.button_move['state'] = 'disabled'

    @staticmethod
    def __set_size__(root):
        width_window_min_size = int(root.winfo_screenwidth() / 3)
        height_window_min_size = int(root.winfo_screenheight() / 2)

        root.minsize(width_window_min_size, height_window_min_size)

        root.geometry('{}x{}'.format(width_window_min_size,
                                     height_window_min_size))

    def __start_button_act__(self):
        # Получение значения текста (строки) и проверка
        self._model.string = self._side_panel.text.get(1.0, 'end')[0:-1]
        if len(self._model.string) == 0:
            self._model.string = 'Введите текст'
            self._side_panel.text.insert(1.0, self._model.string)
        # Получение значения подстроки и проверка
        self._model.pattern = self._side_panel.pattern_entry.get()
        if len(self._model.pattern) == 0:
            self._model.pattern = 'Введите текст'
            self._side_panel.pattern_entry.insert(1, self._model.pattern)
        # Получить функцию-алгоритм исходя из выбора пользователя
        current_alg = self._side_panel.algorithms_box.get()
        self._model.set_algorithm(current_alg)
        # Заблокировать запись подстроки
        self._side_panel.pattern_entry['state'] = 'disabled'
        # Заблокировать запись текста (строки)
        self._side_panel.text['state'] = 'disabled'
        # Заблокировать выбор алгоритма
        self._side_panel.algorithms_box['state'] = 'disabled'
        # Разблокировать кнопку для применения алгоритма
        self._side_panel.button_move['command'] = self.__make_move_button_act__
        self._side_panel.button_move['state'] = 'normal'
        # Разблокировать кнопку для окончания работы алгоритма
        self._side_panel.button_finish['command'] = self.__finish_button_act__
        self._side_panel.button_finish['state'] = 'normal'
        # Заблокировать кнопку для старта работы алгоритма
        self._side_panel.button_start['state'] = 'disabled'

    def __finish_button_act__(self):
        # Чистим найденные вхождения
        self._model._found_substrings_indexes = []
        # Разблокировать ввод подстроки
        self._side_panel.pattern_entry['state'] = 'normal'
        # Разблокировать ввод текста (строки)
        self._side_panel.text['state'] = 'normal'
        # Разблокировать выбор алгоритма
        self._side_panel.algorithms_box['state'] = 'readonly'
        # Заблокировать кнопку для применения алгоритма
        self._side_panel.button_move['state'] = 'disabled'
        # Разблокировать кнопку для применения алгоритма
        self._side_panel.button_start['command'] = self.__start_button_act__
        self._side_panel.button_start['state'] = 'normal'
        # Заблокировать кнопку для окончания работы алгоритма
        self._side_panel.button_finish['state'] = 'disabled'
        # Чистим от тегов(пометок найденных и текущих индексов)
        self._clear()

    def __make_move_button_act__(self):
        # Удаляем все теги предыдущих "текущих" индексов
        self._side_panel.text.tag_remove('goldbackground', 1.0, 'end')
        # Применяем выбранный алгоритм
        data = self._model.current_algorithm.pass_one_step()
        # Добавляем теги для найденных индексов (окрашиваем в красный)
        for i in data.found_indexes:
            self._side_panel.text.tag_add('redforeground',
                                          f'1.0+{i}c',
                                          f'1.0+{i + len(self._model.pattern)}c')
        # Добавляем теги для текущих индексов (окрашиваем в жёлтый)
        for i in data.current_indexes:
            self._side_panel.text.tag_add('goldbackground', f'1.0+{i}c')
        # Если алгоритм закончил работу, то блок-м кнопку применения алгоритма
        if data.is_over:
            self._side_panel.button_move['state'] = 'disabled'

    def _clear(self):
        self._side_panel.text.tag_remove('redforeground', 1.0, 'end')
        self._side_panel.text.tag_remove('goldbackground', 1.0, 'end')
