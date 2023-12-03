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

        q = 0
        for i in range(n):
            while q > 0 and not self.cmp(pattern[q], text[i]):
                q = kmp_table[q - 1]
            if self.cmp(pattern[q], text[i]):
                q += 1
            if q == m:
                occurrences.append(i - m)
                q = kmp_table[q - 1]

        return occurrences
