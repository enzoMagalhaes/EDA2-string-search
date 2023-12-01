from .AbsStringMatch import AbsStringMatch


class KMP(AbsStringMatch):
    def build_kmp_table(pattern):
        table = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j - 1]

            if pattern[i] == pattern[j]:
                j += 1

            table[i] = j

        return table

    def search(self, text, pattern):
        self.iteration_counter = 0
        if not text or not pattern:
            return []

        m, n = len(pattern), len(text)
        kmp_table = KMP.build_kmp_table(pattern)
        occurrences = []

        i = j = 0
        while i < n:
            if self.cmp(pattern[j], text[i]):
                i += 1
                j += 1

                if j == m:
                    occurrences.append(i - j)
                    j = kmp_table[j - 1]
            else:
                if j != 0:
                    j = kmp_table[j - 1]
                else:
                    i += 1

        return occurrences
