class TextEditor:
    cur_w = 0
    cur_c = 0

    def __init__(self, txt):
        self.words = self._split_text(txt)
        self.queries = self._build_query_dict()

    def _split_text(self, txt):
        return txt.split(' ')

    def _build_query_dict(self):
        return {
            'forward char': self.forward_char,
            'forward word': self.forward_word,
            'backward char': self.backward_char,
            'backward word': self.backward_word,
            'delete char': self.delete_char,
            'delete word': self.delete_word
        }

    def query(self, q):
        if self._is_insert_query(q):
            txt = self._extract_insert_text(q)
            self.insert(txt)
        else:
            self._run_query(q)

    def _is_insert_query(self, q):
        return q.startswith('i')

    def _extract_insert_text(self, q):
        return q.split(maxsplit=1)[1][1:-1]

    def _run_query(self, q):
        if q in self.queries:
            self.queries[q]()
        else:
            pass

    ### FORWARD CHAR ###
    def forward_char(self):
        if self._can_forward_char_current_word():
            self._forward_in_current_word()
        elif self._can_forward_word():
            self._goto_next_word_start()
        else:
            pass

    def _can_forward_char_current_word(self):
        return self.cur_c < len(self.words[self.cur_w])

    def _can_forward_word(self):
        return self.cur_w < len(self.words) - 1

    def _forward_in_current_word(self):
        self.cur_c += 1

    def _goto_next_word_start(self):
        self.cur_w += 1
        self.cur_c = 0

    ### FORWARD WORD ###
    def forward_word(self):
        if self._forward_word_inside_word():
            self._jump_to_end_of_current_word()
        elif self._can_forward_word():
            self._forward_word_to_next_nonempty()
        else:
            pass

    def _forward_word_inside_word(self):
        return self.cur_c < len(self.words[self.cur_w])

    def _jump_to_end_of_current_word(self):
        self.cur_c = len(self.words[self.cur_w])

    def _forward_word_to_next_nonempty(self):
        self.cur_w += 1
        self._skip_empty_words_forward()
        self.cur_c = len(self.words[self.cur_w])

    def _skip_empty_words_forward(self):
        while not self._current_word_len() and self.cur_w < len(self.words) - 1:
            self.cur_w += 1

    def _current_word_len(self):
        return len(self.words[self.cur_w])

    ### BACKWARD CHAR ###
    def backward_char(self):
        if self._can_backward_char_current_word():
            self._backward_in_current_word()
        elif self._can_backward_word():
            self._goto_prev_word_end()
        else:
            pass

    def _can_backward_char_current_word(self):
        return self.cur_c > 0

    def _can_backward_word(self):
        return self.cur_w > 0

    def _backward_in_current_word(self):
        self.cur_c -= 1

    def _goto_prev_word_end(self):
        self.cur_w -= 1
        self.cur_c = len(self.words[self.cur_w])

    ### BACKWARD WORD ###
    def backward_word(self):
        if self._backward_word_inside_word():
            self._jump_to_start_of_current_word()
        elif self._can_backward_word():
            self._backward_word_to_prev_nonempty()
        else:
            pass

    def _backward_word_inside_word(self):
        return self.cur_c > 0

    def _jump_to_start_of_current_word(self):
        self.cur_c = 0

    def _backward_word_to_prev_nonempty(self):
        self.cur_w -= 1
        self._skip_empty_words_backward()

    def _skip_empty_words_backward(self):
        while not len(self.words[self.cur_w]) and self.cur_w > 0:
            self.cur_w -= 1

    ### INSERT ###
    def insert(self, txt):
        st = self._split_insert_text(txt)
        new_words = self._prepare_new_words_prefix()
        if self._multiple_words_to_insert(st):
            self._insert_multiple_words(st, new_words)
        else:
            self._insert_single_word(st, new_words)
        self._finish_insert_update(st, new_words)

    def _split_insert_text(self, txt):
        return txt.split(' ')

    def _prepare_new_words_prefix(self):
        return self.words[:self.cur_w]

    def _multiple_words_to_insert(self, st):
        return len(st) > 1

    def _insert_multiple_words(self, st, new_words):
        cw = self.words[self.cur_w]
        new_words.append(self._compose_insert_word_begin(cw, st[0]))
        self._append_mid_new_words(st, new_words)
        new_words.append(self._compose_insert_word_end(st[-1], cw, self.cur_c))
        self.cur_c = len(st[-1])

    def _compose_insert_word_begin(self, cw, first_st):
        return cw[:self.cur_c] + first_st

    def _append_mid_new_words(self, st, new_words):
        new_words.extend(st[1:-1])

    def _compose_insert_word_end(self, last_st, cw, cur_c):
        return last_st + cw[cur_c:]

    def _insert_single_word(self, st, new_words):
        cw = self.words[self.cur_w]
        new_words.append(self._combine_single_insert(cw, st[0]))
        self.cur_c += len(st[0])

    def _combine_single_insert(self, cw, st0):
        return cw[:self.cur_c] + st0 + cw[self.cur_c:]

    def _finish_insert_update(self, st, new_words):
        new_words.extend(self.words[self.cur_w + 1:])
        self.cur_w += len(st) - 1
        self.words = new_words

    ### DELETE CHAR ###
    def delete_char(self):
        cw = self.words[self.cur_w]
        if self._can_delete_char(cw):
            self._delete_from_current_word(cw)
        elif self._can_join_next_word(cw):
            self._merge_with_next_word(cw)
        else:
            pass

    def _can_delete_char(self, cw):
        return self.cur_c < len(cw)

    def _delete_from_current_word(self, cw):
        self.words[self.cur_w] = cw[:self.cur_c] + cw[self.cur_c + 1:]

    def _can_join_next_word(self, cw):
        return self.cur_w < len(self.words) - 1

    def _merge_with_next_word(self, cw):
        if self._current_word_len():
            nw = self.words.pop(self.cur_w + 1)
            self.words[self.cur_w] = cw + nw
        else:
            self.words.pop(self.cur_w)

    ### DELETE WORD ###
    def delete_word(self):
        if self._can_delete_inside_word():
            self._truncate_current_word()
        elif self._can_delete_next_words():
            self._delete_next_nonempty_words()
        else:
            pass

    def _can_delete_inside_word(self):
        return self.cur_c < len(self.words[self.cur_w])

    def _truncate_current_word(self):
        self.words[self.cur_w] = self.words[self.cur_w][:self.cur_c]

    def _can_delete_next_words(self):
        return self.cur_w < len(self.words) - 1

    def _delete_next_nonempty_words(self):
        tmp_w = self.cur_w + 1
        tmp_w = self._advance_to_next_nonempty_word(tmp_w)
        if self._is_valid_delete(tmp_w):
            self._perform_words_deletion(tmp_w)

    def _advance_to_next_nonempty_word(self, tmp_w):
        while tmp_w < len(self.words) and not len(self.words[tmp_w]):
            tmp_w += 1
        return tmp_w

    def _is_valid_delete(self, tmp_w):
        return tmp_w < len(self.words)

    def _perform_words_deletion(self, tmp_w):
        del self.words[self.cur_w + 1:tmp_w + 1]

    ### OUTPUT ###
    def output(self):
        words = self._copy_words()
        words[self.cur_w] = self._get_caret_word()
        self._print_words(words)

    def _copy_words(self):
        return self.words.copy()

    def _get_caret_word(self):
        return self.words[self.cur_w][:self.cur_c] + '^' + self.words[self.cur_w][self.cur_c:]

    def _print_words(self, words):
        print(*words)


def _read_int():
    return int(input())

def _read_line():
    return input().strip()

def _process_text_editor_case():
    te = _create_text_editor()
    q = _read_int()
    for _ in range(q):
        _handle_query(te)
    te.output()

def _create_text_editor():
    return TextEditor(_read_line())

def _handle_query(te):
    te.query(_read_line())

def _main():
    n = _read_int()
    for _ in range(n):
        _process_text_editor_case()

_main()