from .AbsStringMatch import AbsStringMatch
from collections import defaultdict


class BMH(AbsStringMatch):
    def bad_char_table(pattern, m):
        table = defaultdict(lambda: m)
        for k in range(m - 1):
            table[ord(pattern[k])] = m - k - 1
        return table

    def search(self, text, pattern):
        self.iteration_counter = 0
        m = len(pattern)
        n = len(text)

        if m > n:
            return -1

        bad_char_table = BMH.bad_char_table(pattern, m)
        occurrences = []

        k = m - 1
        while k < n:
            j = m - 1
            i = k
            while j >= 0 and self.cmp(text[i], pattern[j]):
                j -= 1
                i -= 1
            if j == -1:
                occurrences.append(i + 1)

            k += bad_char_table[ord(text[k])]

        return occurrences
